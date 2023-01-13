import tkinter as tk
from tkinter import *

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = Tk()
window.title('justpython')
window.minsize(width=400, height=400)

title_label = Label(master=window, text='เมื่อรักฉันเกิด')
title_label.pack()

text_input = Entry(master=window)
text_input.pack()

okay_button = Button(master=window, text="Okay", command=set_message)
okay_button.pack()

window.mainloop()