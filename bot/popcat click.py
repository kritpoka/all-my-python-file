from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
n=1
while keyboard.is_pressed('q') == False:
    
    click(x=734,y=401)
    print(n)
    n= n+1
    time.sleep(0.5)
