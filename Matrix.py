import numpy as n
from tkinter import *
r=Tk()
r(500,500)
def creatematrix():
    def mat(r, c):
        l = []
        for i in range(0, r):
            l.append([0])
            for j in range(0, c - 1):
                x = l[i]
                x.append(0)
                l[i] = x
        return l

    def matval():
        for i in range(0, row):
            for j in range(0, col):
                matrix[i][j] = int(input(f"Enter the value for a{i + 1}{j + 1}:"))
        return matrix

    rowcolm = input('Enter the order of the matrix:')
    l1 = rowcolm.split('x')
    row = int(l1[0])
    col = int(l1[1])
    m = mat(row, col)
    matrix = n.array(m)
    m1 = matval()
    print(m1)
    return m1
r.mainloop()
