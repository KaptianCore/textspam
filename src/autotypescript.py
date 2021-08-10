import pyautogui, time
import random
import keyboard
import os
cwd = os.getcwd()
time.sleep(5)
scripts = ["bee","shrek","strictlyballroom","emoji","rickroll"]
n = open(f"{cwd}/scripts/{random.choice(scripts)}", 'r')
# n = open(f"{cwd}/scripts/beemoviescriptthing/pi", 'r')
for word in n:
    if keyboard.is_pressed('ESC'):
        print('Exiting Random Script Spam')
        break
    else:
        pyautogui.typewrite(word)