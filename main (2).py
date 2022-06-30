from tkinter import *
from tkinter import messagebox
import numpy as np
import oprators as f
funt= f.drpdwn()
import input_matrix as t


def mat(r, c):
    l = []
    for i in range(0, r):
        l.append([0])
        for j in range(0, c - 1):
            x = l[i]
            x.append(0)
            l[i] = x
    return l





def creatematrix1(r,c):

    root = Tk()
    root.title("Matrix")
    root.geometry("250x200")
    root.configure(bg='bisque2')

    text_var = StringVar
    entries = StringVar
    text_var = []
    entries = []

    def get_mat():
        global matrix1
        matrix1 = []
        for i in range(r):
            matrix1.append([])
            for j in range(c):
                matrix1[i].append(int(text_var[i][j].get()))
        matrix1=np.array(matrix1)
        root.destroy()
        print(matrix1)



    Label(root, text="Enter matrix 1:", font=('arial', 10, 'bold'),
          bg="bisque2").place(x=20, y=20)


    x2 = 0
    y2 = 0
    for i in range(r):
        text_var.append([])
        entries.append([])
        for j in range(c):
            text_var[i].append(StringVar())
            entries[i].append(Entry(root, textvariable=text_var[i][j], width=3))
            entries[i][j].place(x=60 + x2, y=50 + y2)
            x2 += 30

        y2 += 30
        x2 = 0
    button = Button(root, text="Submit", bg='bisque3', width=15, command=get_mat)

    button.pack(side= BOTTOM)


    root.mainloop()
def creatematrix2(r, c):
    window = Tk()
    window.title("Matrix")
    window.geometry("250x200")
    window.configure(bg='bisque2')

    text_var = StringVar
    entries = StringVar
    text_var = []
    entries = []

    def get_mat():
        global matrix2
        matrix2 = []
        for i in range(r):
            matrix2.append([])
            for j in range(c):
                matrix2[i].append(int(text_var[i][j].get()))
        matrix2 = np.array(matrix2)
        print(matrix2)
        window.destroy()

    Label(window, text="Enter matrix 2:", font=('arial', 10, 'bold'),
            bg="bisque2").place(x=20, y=20)

    x2 = 0
    y2 = 0
    for i in range(r):

        text_var.append([])
        entries.append([])
        for j in range(c):
            text_var[i].append(StringVar())
            entries[i].append(Entry(window, textvariable=text_var[i][j], width=3))
            entries[i][j].place(x=60 + x2, y=50 + y2)
            x2 += 30

        y2 += 30
        x2 = 0
    button = Button(window, text="Submit", bg='bisque3', width=15, command=get_mat)

    button.pack(side=BOTTOM)

    window.mainloop()
def multiply(matrix1,matrix2):
    m1 = matrix1
    m2= matrix2
    def mat(r, c):
        l = []
        for i in range(0, r):
            l.append([0])
            for j in range(0, c - 1):
                x = l[i]
                x.append(0)
                l[i] = x
        return l
    result=mat(len(m1),len(m2[0]))

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    result=np.array(result)
    return result

rc1 = t.odrmat1()
def oprators (funt):
    if funt == "multiplication":
        rc2 = t.odrmat2()
        r1 = int(rc1[0])
        c1 = int(rc1[1])
        r2 = int(rc2[0])
        c2 = int(rc2[1])
        if c1 == r2:
            creatematrix1(r1, c1)
            print(f'{funt}')
            creatematrix2(r2, c2)
            mat_mul=(multiply(matrix1,matrix2))
            def destroy():
                win1.destroy()
            win1 = Tk()
            win1.geometry("200x200")
            label = Label(win1, text=f"{mat_mul}").pack()
            btn = Button(win1, text="okay", command=destroy).pack()
            print(mat_mul)
            win1.mainloop()

        else:
            r = Tk()
            r.geometry("300x200")
            w = Label(r, text='Waring', font="70")
            messagebox.showerror("THis cant be done", "This matrix cant be multipled")
            r.mainloop()


    elif funt=="add" or funt== "subraction" or funt=="inverse":
        r = int(rc1[0])
        c = int(rc1[1])
        creatematrix1(r, c)
        creatematrix2(r, c)
        if funt == "add":
            def destroy():
                win1.destroy()
            mat_add = np.add(matrix1, matrix2)
            win1 = Tk()
            win1.geometry("200x200")
            label = Label(win1, text=f"{mat_add}").pack()
            btn = Button(win1, text="okay", command=destroy).pack()
            print(mat_add)
            win1.mainloop()



        elif funt == "subraction":
            def destroy():
                win1.destroy()

            mat_sub = np.subtract(matrix1, matrix2)
            win1 = Tk()
            win1.geometry("200x200")
            label = Label(win1, text=f"{mat_sub}").pack()
            btn = Button(win1, text="okay", command=destroy).pack()
            print(mat_sub)
            win1.mainloop()
oprators(funt)
