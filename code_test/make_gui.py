from tkinter import *

def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='just zero!')
        return

    output= ''
    for i in range(1, 13):
        output += str(number) + 'x' + str(i) + '=' + str(number * i) + '\n'
    
    output_label.configure(text=output)

window = Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = Label(master=window, text='multiplication table')
title_label.pack(pady=20)

number_input = Entry(master=window, width=20)
number_input.pack()

go_button = Button(
    master=window, text='show table', command=show_output, width=15
)
go_button.pack(pady=5)

output_label = Label(master=window)
output_label.pack(pady=20)

window.mainloop()