import numpy
def mult(m1,m2):
    a1 = []
    for r in range(0, len(m1)):
        a2 = []
        for c in range(0, len(m2[0])):
            x = 0
            for b in range(0, len(m2[0])):
                for j in range(0, len(m2)):
                    a = m1[b][j] * m2[j][b]
                    x += a
            a2.append(x)
        a1.append(a2)
    a1 = numpy.array(a1)
    return a1
m1=[[5,1],[1,1]]
m2=[[1,5],[5,1]]
a=mult(m1,m2)

print(a)