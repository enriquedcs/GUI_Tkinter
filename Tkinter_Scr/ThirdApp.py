from tkinter import *
import tkinter.messagebox
from io import StringIO


root = Tk()
root.title('Run Python Code')
root.geometry('800x500')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)

def clear_python():
    python_code.delete('1.0', END)


def run():
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    # Run python code
    exec(python_code.get('1.0', END))
    # Show Python code to user
    sys.stdout = old_stdout
    tkinter.messagebox.showinfo('Result', redirected_output.getvalue())


top= Frame(root, width=800, height=80, bg=color)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=420, bg=color)
bottom.pack(side=BOTTOM)

btn_clear = Button(top, text='Clear', highlightbackground=color, font=('arial', 18, 'bold'), command= lambda : clear_python())
btn_clear.pack(side=TOP)

btn_run = Button(top, text='Run', highlightbackground=color, font=('arial', 18, 'bold'), command = lambda : run())
btn_run.pack(side=TOP)

python_code = Text(bottom, font=('arial', 18, 'bold'), bg ='gray88')
python_code.pack(side=TOP)

root.mainloop()