import pyautogui, time
import random
import keyboard
import os
cwd = os.getcwd()
time.sleep(5)
scripts = os.listdir(f"{cwd}/scripts")
n = open(f"{cwd}/scripts/{random.choice(scripts)}", 'r')
# n = open(f"{cwd}/scripts/pi/pi", 'r') This is for personal use :)
for word in n:
    if keyboard.is_pressed('ESC'):
        print('Exiting Random Script Spam')
        break
    else:
        pyautogui.typewrite(word)