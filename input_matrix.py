from tkinter import *
import numpy as n


def odrmat1():
    root = Tk()
    root.geometry("450x250")
    ormat1 = StringVar()

    def show():
        root.destroy()

    root.title("Matrix")

    Label(root, text="Matrix", font=('courier new', 20,)).pack()

    Label(root, text="Order of Matrix :", font=('courier new', 12,)).place(x=10, y=80)

    Entry(root, textvariable=ormat1, width=7).place(x=185, y=80)

    button = Button(root, text="Entry?", command=show).place(x=250, y=80)

    root.mainloop()
    mat1 = ormat1.get()
    mat1 = mat1.split('x')
    return mat1

def odrmat2():
    root = Tk()
    root.geometry("450x250")

    ormat2 = StringVar()

    def show():
        root.destroy()

    root.title("Matrix")

    Label(root, text="Matrix", font=('courier new', 20,)).pack()

    Label(root, text="Order of Matrix 2:", font=('courier new', 12,)).place(x=10, y=80)

    Entry(root, textvariable=ormat2, width=7).place(x=185, y=80)

    button = Button(root, text="Entry?", command=show).place(x=250, y=80)

    root.mainloop()
    mat2 = ormat2.get()
    mat2 = mat2.split('x')
    return mat2
