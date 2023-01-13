from tkinter import *
from tkinter import messagebox
import sys
def mHello():
    print("krit poka")
def hello(evenet):
    #Message Box
    status=messagebox.askyesno(title="คำยืนยัน",message="คุณต้องการปิดหรือไม่")
    if status>0:
        sys.exit()    

# cerate screen 
gui=Tk()
gui.geometry("550x450")
gui.title("Python GUI Basic")

# create text
mLabel=Label(text="Krit poka",fg="black",bg="pink")
mLabel.pack()

# Button 
mButton=Button(text="Submit",fg="red",bg="yellow",command=mHello)
mButton.pack()
b1=Button(text="Hello")
b1.bind('<Button-1>',hello)
b1.pack()

#textbox
objEntry=Entry()
objEntry.pack()

# menu 
menubar=Menu(gui)
# Menu file 
fileMenu=Menu(menubar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save..As")
fileMenu.add_command(label="Close")

#menu help 
helpMenu=Menu(menubar,tearoff=0)
helpMenu.add_command(label="Contact")
helpMenu.add_command(label="Comment")

#menu news
newsMenu=Menu(menubar,tearoff=0)
newsMenu.add_command(label="Facebook")
newsMenu.add_command(label="Instagram")

#add menu
menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Help",menu=helpMenu)
menubar.add_cascade(label="News",menu=newsMenu)
gui.config(menu=menubar)

gui.mainloop()
