from tkinter import *
def mHello():
    print("Krit Poka Button")
gui=Tk()
gui.geometry("500x450")
gui.title("Python GUI Basic")
mlabel=Label(text="Welcome",fg="black",bg="pink") 
mlabel.pack()
mButton=Button(text="Submit",fg="red",bg="yellow",command="mHello") 
mButton.pack()
gui.mainloop()
