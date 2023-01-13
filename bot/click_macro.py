from tkinter.constants import COMMAND
from typing import Text
import pyautogui
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con
import tkinter as tk

def click():
    #win32api.SetCursorPos(())
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.00001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def macro():
    n=1 
    while keyboard.is_pressed('ctrl + alt') == False:
        #text_label.configure(text='activated press alt + ctrl for disable')
        if keyboard.is_pressed('left alt'):
            click()
            print(n)
            n= n+1

def status_change():
    text_label.configure(text='activated press alt + ctrl for disable')

root = tk.Tk()
root.title('macro mouse')
root.minsize(width=400, height=400)

text_label = tk.Label(master=root, text='disable')
text_label.pack()

activate_button = tk.Button(master=root, text='activate macro', command=lambda:[macro(),status_change()])
activate_button.pack()

root.mainloop()

        
