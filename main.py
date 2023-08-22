import datetime
import time
import pyautogui
import pygetwindow as gw
import pytesseract
from PIL import Image, ImageEnhance

error_codes = ["277", "268", "264", "529", "279", "266", "267", "279"] #edit this list to match the errors you want
output_file = "error_log.txt"

# Define the enhancement factor for brightness and contrast
BRIGHTNESS_FACTOR = 1.5
CONTRAST_FACTOR = 1.5
def main():

    while True:
        windows = gw.getWindowsWithTitle('image')

        for window in windows:
            window_title = window.title
            window_index = windows.index(window)

            window.minimize()
            window.restore()
            time.sleep(0.5)

            if window.isActive:
                screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
                enhanced_screenshot = enhance_image(screenshot)
                enhanced_screenshot.save(f'screenshots/screenshot {window_index}.png')

                ocr_result = perform_ocr(f'screenshots/screenshot {window_index}.png')
                for error_code in error_codes:
                    if f"Error Code: {error_code}".replace(" ", "").lower() in ocr_result.replace(" ", "").lower():
                        error_message = f"Found Error Code: {error_code} in window: {window_title}"
                        save_error_to_file(error_message)
                        print(error_message)
                        window.close()
                        window_closed_alert = f"closed window{window_title}"
                        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  closed window {window_title}")
                        save_error_to_file(window_closed_alert)

        time.sleep(300)




def perform_ocr(image_path):
    img = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(img)
    return ocr_result

def save_error_to_file(error_message):
    timestamp = datetime.datetime.now()
    with open(output_file,  "a", encoding="utf-8") as file:
        file.write(timestamp.replace(microsecond=0).strftime('%Y-%m-%d %H:%M:%S') + ":  " + error_message + "\n")

def enhance_image(image):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(BRIGHTNESS_FACTOR)

    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(CONTRAST_FACTOR)

    return enhanced_image

if __name__ == "__main__":
    main()
