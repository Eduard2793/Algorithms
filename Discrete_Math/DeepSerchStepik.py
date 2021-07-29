# определение числа компонент связности
# по ходу находятся и записываются пути и остовные деревья
# Failed test #5 of 16. Wrong answer
import numpy as np

ve = input().split(" ")
v = int(ve[0])
e = int(ve[1])

def Graf():
    graf = True
    if e <= 0 or v <= 1:
        graf = False
    return graf


graf = Graf()
if graf:
    matrix = np.zeros((v,v))
    for i in range(0,e):
        reb = input().split(" ")
        x = int(reb[0]) - 1
        y = int(reb[1]) - 1
        if x + 1 > v or y + 1 > v:
            graf = False
            break
        matrix[x][y] = 1
        matrix[y][x] = 1

if graf:
    def pasFinder(start,pas):
        q = start
        flag = True
        while flag:
            for ver in range(v):
                if ver == q:
                    pas.append(ver)
                    for i in range(0,matrix[0].size):
                        if matrix[ver][i] == 1:
                            matrix[ver][i] = matrix[i][ver] = 2
                            q = i
                            break
            if pas[len(pas)-1] == q:
                r = q
                for j in range(v):
                    if j not in pas:
                        q = j
                        pas.append(-1)
                        break
                if r == q:
                    flag = False
            

    pas = []            
    pasFinder(0,pas)
    pas.append(-1)
    
    Pas = []
    arr = []
    for x in pas:
        if x != -1:
            arr.append(x)
        else:
            Pas.append(arr)
            arr = []


    stuff = True
    t = len(Pas)
    while stuff:
        flag = False
        n = len(Pas)
        for i in range(n):
            if flag:
                break
            else:
                for j in range(0,len(Pas[i])):
                    if flag:
                        break
                    else:
                        for p in Pas:
                            if flag:
                                break
                            else:
                                if p != Pas[i]:
                                    if Pas[i][j] in p:
                                        Pas[i].extend(p)
                                        Pas.remove(p)
                                        t = len(Pas)
                                        flag = True
        if n == t:
            stuff = False
            
    print(len(Pas))

else:
    if e == 0:
        print(v)
    else:
        print(0)

































        

    
