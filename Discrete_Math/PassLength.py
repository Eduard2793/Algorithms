# пойск в ширину для определеия расстояний
# Failed test #2 of 21. Time limit exceeded
class myList(list):
    def ad(self,x):
        self.reverse()
        self.append(x)
        self.reverse()
    def rem(self):
        return self.pop()

import numpy as np

ve = input().split(" ")
v = int(ve[0])
e = int(ve[1])
matrix = np.zeros((v,v))
for i in range(0,e):
    reb = input().split(" ")
    x = int(reb[0])
    y = int(reb[1])
    matrix[x][y] = matrix[y][x] = 1

Q = myList()
levels = {}

def foo():
    while len(Q) != 0:
        ver = Q.rem()
        arr = []
        for i in range(v):
            if matrix[ver][i] == 1 and matrix[i][i] == 0:
                Q.ad(i)
                matrix[i][i] = 2
                arr.append(i)
        levels[ver] = arr  
        
matrix[0][0] = 2
Q.ad(0)
foo()
it = 0

def Foo(a,b):
    global it
    pred = b
    while a != pred:
        for i in range(v):
            if pred in levels[i]:
                pred = i
                it += 1
                break

arr = []
for i in range(v):
    it = 0
    Foo(0,i)
    arr.append(it)

print(arr)


# тоже самое но рекурсивно:        
'''
def foo():
    if len(Q) == 0:
        return
    else:
        ver = Q.rem()
        arr = []
        for i in range(v):
            if matrix[ver][i] == 1 and matrix[i][i] == 0:
                Q.ad(i)
                #matrix[ver][i] = matrix[i][ver] = 2
                matrix[i][i] = 2
                arr.append(i)
        levels[ver] = arr                
        foo()
'''

'''
def Foo(a,b): # pass from a to b
    global it
    pred = -1
    if a == b:
        return
    else:
        for i in range(v):
            if b in levels[i]:
                pred = i
                it += 1
                break
        Foo(a,pred)
'''





















