from tkinter import *

root = Tk()
root.title('Test')
root.geometry('200x200')
root.resizable(width=False, height=False)

name = StringVar()

def print_name():
    name.set("Alxzekix")


btn = Button(root, text='click me', command= lambda : print_name())
btn.place(x=10,y=30)

label = Label(root, textvariable=name)
label.place(x=80, y=100)

root = mainloop()


