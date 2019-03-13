from tkinter import *

root = Tk()
root.title('Test')
root.geometry('300x300')
root.resizable(width=False, height=False)

entry = Entry(root)
entry.place(x=50, y=0)

def get_name():
    label1 = Label(root, text=entry.get())
    label1.place(x=100,y=150)


label = Label(root, text='Name')
label.place(x=0, y=0)

btn = Button(root, text='get name', command= lambda : get_name())
btn.place(x=100,y=100)

root.mainloop()