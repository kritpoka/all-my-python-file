from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)
    

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#color of center: (255, 87, 34)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(270, 230, 800, 480))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 34:
                click(x+270,y+230)
                time.sleep(0.05)
                break

            
            
    
