from tkinter import *
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

# ======================================Settings==================================================================================================
root = Tk()
root.title('Email Sender')
color = 'gray30'
root.geometry('800x500')
root.resizable(width=False, height=False)
root.configure(bg=color)
# ======================================Settings===================================================================================================
def clear_from():
    f.delete(0,END)

def clear_to():
    t.delete(0,END)

def clear_all():
    clear_from()
    clear_to()
    message.delete('1.0', END)

def send_email(message):
    HOST = 'smtp.gmail.com'
    PORT = 587

    USERNAME = 'enrique.decoss@gmail.com'
    PASSWORD = 'Zekix1883$'

    SENDER = 'enrique.decoss@gmail.com'
    RECIPIENT = 'email@gmail.com'

    text_subtype = 'plain'

    msg = MIMEText(message, text_subtype)

    msg['Subject'] = 'Python Script'
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    try:
        connection = SMTP(HOST, PORT)
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(SENDER, RECIPIENT, msg.as_string())
    except Exception as e:
        print(e)


# ====================================Frames=======================================================================================================

top= Frame(root, width=800, height=50, bg=color)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=50, bg=color)
bottom.pack(side=BOTTOM)

left = Frame(root, width=600, height=400, bg=color)
left.pack(side=LEFT)

right = Frame(root, width=240, height=400, bg=color)
right.pack(side=RIGHT)

# =================================Buttons===========================================================================================================

btn_clear_from = Button(right, text='Clear from', highlightbackground=color, font=('arial', 16, 'bold'), command= lambda : clear_from())
btn_clear_from.pack(side=TOP)

btn_clear_to = Button(right, text='Clear to', highlightbackground=color, font=('arial', 16, 'bold'), command= lambda : clear_to())
btn_clear_to.pack(side=TOP)

btn_clear_all = Button(right, text='Clear all', highlightbackground=color, font=('arial', 16, 'bold'), command= lambda : clear_all())
btn_clear_all.pack(side=TOP)

send = Button(right, text='Send', highlightbackground=color, font=('arial', 16, 'bold'), command= lambda : send_email(message))
send.pack(side=TOP)

# =================================Entry+Labels======================================================================================================

from_label = Label(top, font=('arial', 16, 'bold'), text='From:', bg=color)
from_label.place(x=10,y=7)

f = Entry(top, font=('arial', 16, 'bold'), width=25, bd=5)
f.place(x=75,y=8)

to_label = Label(top, font=('arial', 16, 'bold'), text='To:', bg=color)
to_label.place(x=400,y=6)

t = Entry(top, font=('arial', 16, 'bold'), width=25, bd=5)
t.place(x=440,y=7)

# =================================MessageBox================================================-------------------------------------------------========

message = Text(left, font=('arial', 16, 'bold'), width=55)
message.pack(side=LEFT)


root.mainloop()