from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position:X:  542 Y:  650 RGB: (178, 183, 234)
#Tile 2 Position:X:  661 Y:  650 RGB: (163, 169, 232)
#Tile 3 Position:X:  719 Y:  650 RGB: (168, 173, 232)
#Tile 4 Position:X:  805 Y:  650 RGB: (169, 173, 233)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(542,550)[0] == 0:
               click(542,565)
    if pyautogui.pixel(661,550)[0] == 0:
               click(661,565 )
    if pyautogui.pixel(719,550)[0] == 0:
               click(719,565)
    if pyautogui.pixel(805,550)[0] == 0:
               click(805,565)

