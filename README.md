# windowsAutoCloser
IMPORTANT TO DO FIRST:
for tesseract do the following: 
1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

to run the project, first set up your virtual environement:
python -m venv venv

then activate it:
source venv/bin/activate  
On Windows: .\venv\Scripts\activate

pip install -r requirements.txt

open cmd, then "cd path/to/the/script/folder" then run "python main.py"

NOTE: by default, the name of windows to be scanned must start with "Roblox", the scan will automatically be done
after every 15min (900 seconds), and the windows to be closed need to have these error codes 
["277", "268", "264", "529", "279", "266", "267", "279"] preceded by the string "Error Code: ":
there's a process time of 0.5 seconds for each window.

if you wish to have a different setting, then open the main.py file, and at the top you will find the parameters, update accordingly.

dm green.beret (discord) for issues 



