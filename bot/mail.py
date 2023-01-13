from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def opens():
    n = 1 
    while n == 1 :
        if pyautogui.locateOnScreen('Chrom.png', confidence=0.8)!=None:
            i = pyautogui.locateOnScreen('Chrom.png', confidence=0.8)
            time.sleep(1)
            click(i,clicks=2)
            time.sleep(1) 
            write('gmail.com')
            press('Enter')
            n += 1 
        else:
            print("I am unable to see it")
            time.sleep(1)

def find_mail():
    i = 1 
    while i == 1 :
        if pyautogui.locateOnScreen('Fmail.png', confidence=0.8)!=None:
            f = pyautogui.locateOnScreen('Fmail.png', confidence=0.8)
            click(f)
            i += 1
            time.sleep(1)
  
def find_mail_two():
    k=1 
    while k==1 :
        if pyautogui.locateOnScreen('9189.png', confidence=0.8) != None:
            s = pyautogui.locateOnScreen('9189.png', confidence=0.8)
            click(s)
            k += 1 

           
   
opens()
find_mail()
find_mail_two()



    

    
