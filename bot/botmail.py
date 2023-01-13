from numpy import percentile
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
    

def opens():

#input data 
    print('1.gmail')
    print('2.classroom')
    print('3.google keep')
    print('4.mail and classroom')
    choose = int(input('choose number: '))

#open
    n = 1 
    while n == 1 :
        if pyautogui.locateOnScreen('Chrom.png', confidence=0.8)!=None:
            i = pyautogui.locateOnScreen('Chrom.png', confidence=0.8)
            time.sleep(1)
            click(i,clicks=2)
            time.sleep(2) 
            if choose == 1:
                write('mail.google.com/mail/u/1')
                press('Enter')
            elif choose == 2:
                write('classroom.google.com/u/1/h')
                press('Enter')
            elif choose == 3:
                write('keep.google.com')
                press('Enter')
            else:
                write('mail.google.com/mail/u/1')
                press('Enter')
                keyDown('ctrl')
                keyDown('t')
                keyUp('t')
                keyUp('ctrl')
                write('classroom.google.com/u/1/h')
                press('Enter')
            n += 1 
            
        else:
            press('win')
            write('chrome')
            press('Enter')
            time.sleep(2) 
            if choose == 1:
                write('mail.google.com/mail/u/1')
                press('Enter')
            elif choose == 2:
                write('classroom.google.com/u/1/h')
                press('Enter')
            elif choose == 3:
                write('keep.google.com')
                press('Enter')
            else:
                write('mail.google.com/mail/u/1')
                press('Enter')
                keyDown('ctrl')
                keyDown('t')
                keyUp('t')
                keyUp('ctrl')
                write('classroom.google.com/u/1/h')
                press('Enter')
            n += 1 

#test function 
def test():
    keyDown('ctrl')
    keyDown('a')
    keyUp('a')
    keyUp('ctrl')
opens()
#test()



    

    
