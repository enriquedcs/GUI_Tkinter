from tkinter import *

root = Tk()
root.title('Metric System ')
root.geometry('300x180')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg='gray')

v = IntVar()
res = IntVar()

def cal_price():
    value = int(v.get())

    if value == 0:
        res.set(float(entry.get())*1.609344)
    elif value ==1:
        res.set(float(entry.get()) *29.573530)
    elif value==2:
        res.set(float(entry.get()) * 2.54)


label = Label(root, text='Choose Conversion', bg=color)
label.place(x=110, y=5)

r_btn = Radiobutton(root, text= 'Miles to KM', bg=color, variable=v, value=0)
r_btn.place(x=5, y=30)

r_btn = Radiobutton(root, text= 'Oz to ML', bg=color, variable=v, value=1)
r_btn.place(x=5, y=50)

r_btn = Radiobutton(root, text= 'Inches to Cm', bg=color, variable=v, value=2)
r_btn.place(x=5, y=70)

entry = Entry(root, width=25)
entry.place(x=80, y=120)

label_res = Label(root, text='Value:', bg='gray')
label_res.place(x=5, y=145)

entry_2 = Entry(root, width=25, textvariable=res)
entry_2.place(x=80, y=145)

btn = Button(root, text='Calc', highlightbackground=color, command= lambda : cal_price())
btn.place(x=5, y=120)

root.mainloop()