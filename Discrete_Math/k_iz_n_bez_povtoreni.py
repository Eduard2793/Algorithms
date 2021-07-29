import numpy as np
import math as m

nk = input()
nkL = nk.split(" ")
n = int(nkL[0])
k = int(nkL[1])

def sochnum(p,q):
    if q == p or q == 0:
        return 1
    else:
        return sochnum(p-1,q-1)+sochnum(p-1,q)

def combnum(p,q):
    s = sochnum(p,q)
    return m.factorial(q)*s



def Function():
    arr = np.zeros(k)
    cbn = combnum(n,k)
    matrix = np.zeros((cbn,k))
    foo(matrix,k)
    return matrix
        
            
combNum = 0
z = np.zeros(n)
'''
def foo(matrix, arr, countArr, last, n):
    global combNum
    if countArr == 0:
        for i in range(0,len(arr)):
            matrix[combNum][i] = arr[i]
        combNum += 1
        return
    for i in range(last+1,n):
        arr[len(arr) - countArr] = i
        foo(matrix,arr,countArr-1,i,n)
'''        

def X(start,n,k):
    arr = []
    for i in range(0,n):
        arr[start] = i
        
        
'''
def foo(matrix,countArr):
    if countArr == 0:
        return
    arr = np.zeros(k)
    global combNum
    for j in range(0,countArr):
        arr[j] = j
    for i in range(countArr-1,n):
        arr[countArr-1] = i
        matrix[combNum] = arr
        combNum += 1
    countArr = countArr - 1
    foo(matrix,countArr)
    
matr = Function()
'''
def matrPrint(matrix):
    f = int(matrix.size/matrix[0].size)
    if matrix[0].size == 0:
        print()
    else:
        for i in range(0,f):
            for j in range(0,matrix[0].size):
                print(int(matrix[i][j]),' ',end='')
            print()


matrix = []


