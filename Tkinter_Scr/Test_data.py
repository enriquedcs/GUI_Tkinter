"""
Author: Enrique Decoss
@package: Tkinter, faker, csv, json
"""

"""
More data

#fake.first_name()
#fake.last_name()
#fake.postalcode()
#fake.company()
#fake.credit_card_expire
#fake.credit_card_security_code
#fake.street_name
#fake.city()
"""

from tkinter import *
from faker import *
import json
import csv
import os

root = Tk()
root.title('Generator')
root.geometry('300x180')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg='gray')

v = IntVar()
res = StringVar()
dir_path = os.getcwd()
fake = Faker()

def test_gencsv(count=10,name_file="Test_data.csv"):

    RECORD_COUNT = count
    with open(name_file, "w", newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'address', 'postalcode', 'city', 'state',
                      'company']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'email': fake.email(),
                    'address': fake.street_name(),
                    'postalcode': fake.postalcode(),
                    'city': fake.city(),
                    'state': fake.state(),
                    'company': fake.company()
                }

            )


def test_genjson(count=10,name_file="Test_data.txt"):

    RECORD_COUNT = count
    data = []
    for i in range(RECORD_COUNT):
        people = {'first_name': fake.name(),
                  'last_name': fake.last_name(),
                  'email': fake.email(),
                  'address': fake.street_name(),
                  'postalcode': fake.postalcode(),
                  'city': fake.city(),
                  'state': fake.state(),
                  'company': fake.company()
                  }
        data.append(people)


    jsonData = json.dumps(data)
    with open(name_file, "w") as f:
        f.write(jsonData)




def generate():
    value = int(v.get())
    count = int(entry.get())

    if value == 0:
        name = "Test_data" + str(count) + ".csv"
        test_gencsv(count, name)
        res.set(dir_path)
    elif value ==1:
        name = "Test_data" + str(count) + ".txt"
        test_genjson(count, name)
        res.set(dir_path)
    elif value==2:
        test_gencsv(count, name)
        res.set(dir_path)


label = Label(root, text='Test Data Generator', bg=color)
label.place(x=110, y=5)

r_btn = Radiobutton(root, text= 'Generate CSV', bg=color, variable=v, value=0)
r_btn.place(x=5, y=30)

r_btn = Radiobutton(root, text= 'Generate JSON', bg=color, variable=v, value=1)
r_btn.place(x=5, y=50)

r_btn = Radiobutton(root, text= 'Generate ...', bg=color, variable=v, value=2)
r_btn.place(x=5, y=70)

label_count = Label(root, text='# Records:', bg='gray')
label_count.place(x=5, y=110)

entry = Entry(root, width=7)
entry.place(x=70, y=110)

label_res = Label(root, text='Path:', bg='gray')
label_res.place(x=5, y=145)

entry_2 = Entry(root, width=25, textvariable=res)
entry_2.place(x=50, y=145)

btn = Button(root, text='Generate', highlightbackground=color, command= lambda : generate())
btn.place(x=230, y=145)

root.mainloop()