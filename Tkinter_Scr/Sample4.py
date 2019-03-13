from tkinter import *

root = Tk()
root.title('Test')
root.geometry('500x500')
root.resizable(width=False, height=False)

frame1 = Frame(root, width=250, height=500, bg='blue')
frame1.pack(side=LEFT)

frame2 = Frame(root, width=250, height=500, bg='red')
frame2.pack(side=RIGHT)

root.mainloop()