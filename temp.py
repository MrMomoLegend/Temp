import pickle as p
from tkinter import *

# User Interface
win = Tk()
win.title("Account Manager")
win.geometry('450x200')

# Input from the user
nvar = StringVar()
pvar = StringVar()

# importing the passwords and usernames and storing in variable
with open(r'C:\Users\Mokith\Downloads\Softwares\log.dat', 'rb') as x:
    try:
        data = p.load(x)
        print(data)

    except EOFError:
        pass
d = data

# --------------------------------------------------------------------
global pinp


# Frontend


def signin():
    head = Label(text="Signin")
    head.pack()
    Label(text='Username:').place(x=40, y=40)
    Label(text='Password:').place(x=40, y=80)
    Entry(width=30, textvariable=nvar).place(x=130, y=40)  # username
    Entry(width=30, textvariable=pvar, show='*').place(x=130, y=80)  # password
    s = Button(text='Submit', command=lambda: out('signin')).place(x=40, y=130)


def signup():
    global pinp
    head = Label(text="Signup")
    head.pack()
    Label(text='Username:').place(x=40, y=40)
    Label(text='Password:').place(x=40, y=80)
    Label(text='Re-Enter Password:').place(x=20, y=120)
    Entry(width=30, textvariable=nvar).place(x=130, y=40)  # username
    Entry(width=30, textvariable=pvar, show='*').place(x=130, y=80)  # password
    Entry(width=30, show='*').place(x=130, y=120)  # re enter password
    Button(text='Submit', command=lambda: out('signup')).place(x=40, y=150)


# --------------------------------------------------------------------------------
def out(inrup):
    username = nvar.get()
    password = pvar.get()
    temp = {}
    if inrup == 'signup':
        temp[username] = password
        d.update(temp)
        with open(r'C:\Users\Mokith\Downloads\Softwares\log.dat', 'wb') as x:
            p.dump(d, x)
        clear()
        signin()
    elif inrup == 'signin':
        if username in d:
            a = d[username]

            if a == password:
                print("Working")
            else:
                print('wrong password')
        else:
            Label(text='username does not exists', font=25, fg='red')
            b = Button(text='Signup', command=lambda: [out('signup')])
            print('no username')


def clear():
    for i in win.winfo_children():
        i.destroy()

    nvar.set('')
    pvar.set('')


signin()
win.mainloop()