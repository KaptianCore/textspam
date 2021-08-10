import pyautogui, time
import random
import keyboard
import os
cwd = os.getcwd()
scripts = os.listdir(f"{cwd}/scripts")
for item in scripts:
    print(item)
scriptChoice = input("Script: ")
if scriptChoice not in scripts:
    print("That doesn't seem to be an option.")
    scriptChoice = input("Script: ")
print(f"Opening Script: {scriptChoice}, Starting Typing In 5 Seconds.")
time.sleep(5)
n = open(f"{cwd}/scripts/{scriptChoice}", 'r')
for word in n:
    if keyboard.is_pressed('ESC'):
        print('Exiting Random Script Spam')
        break
    else:
        pyautogui.typewrite(word)