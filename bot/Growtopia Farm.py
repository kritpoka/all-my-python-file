from pyautogui import *
import keyboard
import pyautogui
import win32api, win32con

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def put():
    win32api.keybd_event(win32con.KEYEVENTF_KEYUP)
    
while keyboard.is_pressed('q') == False:
    click(754,390)
    
        
