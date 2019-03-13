from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('File Counter')
root.geometry('500x500')
color = 'gray'
root.resizable(width=False, height=False)
root.configure(bg=color)

count_result = dict()

def count_text(file):
    file_open = open(str(file),'r')
    full_text = file_open.readlines()
    file_open.close()
    for word in word_list.get().split(' , '):
        for text in full_text:
            if word in count_result:
                count_result[word] = count_result[word] + text.count(word)
            else:
                count_result[word] = text.count(word)

    answer.delete('1.0',END)
    for k, v in count_result.items():
        answer.insert('1.0', '{0} {1} \n'.format(k,v))

    count_result.clear()


def open_file():
    root.filename = filedialog.askopenfilename()

def clear_text():
    word_list.delete(0, END)
    answer.delete('1.0', END)



word_list = Entry(root, width=90)
word_list.place(x=0,y=5)

file = Button(root, text='Select Name', width=70, command= lambda : open_file())
file.place(x=0,y=30)

count = Button(root, text='Count Words',width=70, command= lambda : count_text(root.filename))
count.place(x=0,y=60)

clear = Button(root, text='Clear Text', width=70, command= lambda : clear_text())
clear.place(x=0,y=90)

answer = Text(root, height=30, width=500, bg='gray77')
answer.place(x=0, y=120)


root = mainloop()