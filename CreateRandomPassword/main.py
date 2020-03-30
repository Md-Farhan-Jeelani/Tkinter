from tkinter import *
import datetime
import random

root = Tk()
root.title("Create random password")
root.geometry('400x400')

label1 = Label(root, text='Input length password')
label1.pack()

entry = Entry(root, width=50)
entry.pack()


def createRandomPassword():
    # Create data table include characters from 0-9, a-z, A-Z not including special characters
    string = ''
    asciiCode = [chr(x) for x in range(48, 58)]
    for i in range(65, 91):
        asciiCode.append(chr(i))
    for i in range(97, 123):
        asciiCode.append(chr(i))
    try:
        for i in range(int(entry.get())):
            string += random.choice(asciiCode)
        with open('password.txt', 'a+') as f:
            f.write(string + " {}\n".format(datetime.datetime.now()))
            f.close()
        Label(root, text=string).pack()
    except ValueError:
        Label(root, text="Not valid, Please Input a number").pack()

btn1 = Button(root, text="Create Password", command=createRandomPassword)

btn1.pack()
mainloop()