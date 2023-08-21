# windowsAutoCloser
IMPORTANT TO DO FIRST:
for tesseract do the following: 
1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'


to run the project, first set up your virtual environement:
python -m venv venv

then activate it:
source venv/bin/activate  
# On Windows: .\venv\Scripts\activate

pip install -r requirements.txt

then open the image.png image to test it (you can open the image multiple times if you want to test multiple images)

run "python main.py"

