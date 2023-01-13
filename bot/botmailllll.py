from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

i = 1
while i < 2:
    if pyautogui.locateOnScreen('Chrom.png', confidence=0.8)!=None:
        click('Chrom.png',clicks=2)
        i = i + 1
    else:
        print("I am unable to see it")
        time.sleep(1)
"""
    time.sleep(1) 
    write("gmail.com")
    press('Enter')
"""

"""
j = 1
 while j < 2:
    if pyautogui.locateOnScreen('Fmail.png', confidence=0.8)!=None:
            click('Fmail.png')
    else:
            print("I am unable to see it")
            time.sleep(1)
while 1:
    if pyautogui.locateOnScreen('Smail.png', confidence=0.8)!=None:
            click('Smail.png')
    else:
        print("I am unable to see it")
        time.sleep(1)
"""
    
