import os
import time


os.system("pip install pyinstaller")
time.sleep(1)
os.system("pip install PyQtWebEngine")
time.sleep(1)
os.system("pip install PyQt5")
time.sleep(1)
os.system("pyinstaller --onefile main.py")
time.sleep(1)
os.system("start dist\main.exe")
