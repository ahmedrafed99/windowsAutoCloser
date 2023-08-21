import time
import pyautogui
import pygetwindow as gw
import pytesseract
from PIL import Image

error_codes = ["277", "268", "264", "529", "279", "266", "267"] #add to this list the errors you want
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
                screenshot.save(f'screenshot {windows.index(window)}.png')

                ocr_result = perform_ocr(f'screenshot {windows.index(window)}.png')
                for error_code in error_codes:
                    if f"{error_code}".replace(" ", "") in ocr_result.replace(" ", ""):
                        print(f"Found Error Code: {error_code} in window: {window.title} ")

                        #window.close()
                window.minimize()

        time.sleep(10)




def perform_ocr(image_path):
    img = Image.open(image_path)
    ocr_result = pytesseract.image_to_string(img)
    return ocr_result


if __name__ == "__main__":
    main()
