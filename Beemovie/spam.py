import pyautogui
import time
import keyboard 
time.sleep(5)
f = open("beemovie",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
