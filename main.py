import datetime
import time
import pyautogui
import pygetwindow as gw
import pytesseract
from PIL import Image, ImageEnhance


WINDOW_NAME = "image"  # this is what your window title should start with
ERROR_CODES = ["277", "268", "264", "529", "279", "266", "267", "279"]  # edit this list to match the errors you want
SCAN_PERIOD = 900  # script will scan all windows after every certain period of time, edit value in seconds
output_file = "error_log.txt"

# Define the enhancement factor for brightness and contrast
BRIGHTNESS_FACTOR = 1.5
CONTRAST_FACTOR = 1.5

#after running the script, this folder should contain screenshots of your windows
SCREENSHOT_PATH = "screenshots/"


def main():
    while True:
        print("scanning ..")

        for window in gw.getWindowsWithTitle(WINDOW_NAME):
            process_window(window)

        next_scan_time = currentTime() + datetime.timedelta(seconds=SCAN_PERIOD)
        print(f"next scan at: {next_scan_time.strftime('%H:%M:%S')} ..")
        time.sleep(SCAN_PERIOD)


def process_window(window):

    window.minimize()
    window.restore()
    print(f"processing '{window.title}' ..")
    time.sleep(0.5)

    if window.isActive:
        screenshot = take_screenshot(window)
        enhanced_screenshot = enhance_image(screenshot)
        screenshot_path = save_screenshot(enhanced_screenshot, window)

        try:
            ocr_result = perform_ocr(screenshot_path)
            if check_error_codes(ocr_result, window):
                close_window(window)
        except Exception as e:
            error_message = f"Error processing '{window.title}': {str(e)}"
            save_error_to_file(error_message)
            print(error_message)


def take_screenshot(window):
    return pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))


def save_screenshot(screenshot, window):
    screenshot_path = f"{SCREENSHOT_PATH}{window.title}.png"
    screenshot.save(screenshot_path)
    return screenshot_path

def check_error_codes(ocr_result, window):
    for error_code in ERROR_CODES:
        if f"error code: {error_code}".replace(" ", "").lower() in ocr_result.replace(" ", "").lower():
            error_message = f"Found 'Error Code {error_code}' in '{window.title}' !!"
            save_error_to_file(error_message)
            print(error_message)
            return True
    return False

def perform_ocr(image_path):
    img = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(img)
    return ocr_result


def save_error_to_file(error_message):
    with open(output_file, "a", encoding="utf-8") as file:
        file.write(currentTime().strftime('%Y-%m-%d %H:%M:%S') + ":  " + error_message + "\n")


def enhance_image(image):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(BRIGHTNESS_FACTOR)

    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(CONTRAST_FACTOR)

    return enhanced_image

def close_window(window):
    window.close()
    window_closed_alert = f"Closed '{window.title}'"
    save_error_to_file(window_closed_alert)
    print(f"{currentTime().strftime('%Y-%m-%d %H:%M:%S')}: {window_closed_alert}")

def currentTime():
    return datetime.datetime.now()

if __name__ == "__main__":
    main()
