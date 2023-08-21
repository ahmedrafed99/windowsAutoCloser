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
            window.restore()
            window.activate()
            window.maximize()
            time.sleep(0.5)

            if window.isActive & window.isMaximized:
                screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
                enhanced_screenshot = enhance_image(screenshot)
                enhanced_screenshot.save(f'screenshots/screenshot {windows.index(window)}.png')

                ocr_result = perform_ocr(f'screenshots/screenshot {windows.index(window)}.png')
                for error_code in error_codes:
                    if f"Error Code: {error_code}".replace(" ", "").lower() in ocr_result.replace(" ", "").lower():
                        error_message = f"Error Code: {error_code} in window: {window.title}\n"
                        save_error_to_file(error_message)
                        print(error_message)
                        window.close()
                window.minimize()

        time.sleep(10)




def perform_ocr(image_path):
    img = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(img)
    return ocr_result

def save_error_to_file(error_message):
    timestamp = datetime.datetime.now()
    with open(output_file,  "a", encoding="utf-8") as file:
        file.write(error_message + timestamp.replace(microsecond=0).strftime('%H:%M:%S %Y-%m-%d'))

def enhance_image(image):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(BRIGHTNESS_FACTOR)

    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(CONTRAST_FACTOR)

    return enhanced_image

if __name__ == "__main__":
    main()
