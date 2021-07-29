import numpy as np

ve = input().split(" ")
v = int(ve[0])
e = int(ve[1])

matrix = np.zeros((v,v))

for i in range(0,e):
    xy = input().split(" ")
    x = int(xy[0]) - 1
    y = int(xy[1]) - 1
    matrix[x][y] = matrix[y][x] = 1

    
def isItEiler(matrix):
    for i in range(0,matrix[0].size):
        s = 0
        for j in range(0,matrix[0].size):
            s = s + matrix[i][j]
        if not(s%2 == 0):
            return False

    return True

def findeEiler(matrix):
    if not isItEiler(matrix):
        print("NONE")
        return
    else:
        
