from tkinter import *

root = Tk()
root.title('Test')
root.geometry('300x300')
root.resizable(width=False, height=False)

entry = Entry(root)
entry.place(x=50, y=0)

def get_name():
    print(entry.get())
    entry.insert(0, 'This is a name: ')

label = Label(root, text='Name')
label.place(x=0, y=0)

btn = Button(root, text='get name', command= lambda : get_name())
btn.place(x=100,y=100)



root.mainloop()
