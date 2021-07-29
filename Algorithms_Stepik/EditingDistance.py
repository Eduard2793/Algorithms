
A = input()
B = input()

def EditDist(A,B):
    D = []
    for i in range(len(A)+1):
        row = []
        for j in range(len(B)+1):
            row.append(0)
        D.append(row)

    for i in range(len(A)+1):
        D[i][0] = i
    for i in range(len(B)+1):
        D[0][i] = i
            
      
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            c = 1
            if A[i-1] == B[j-1]:
                c = 0
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + c)
    
    return D[len(A)][len(B)]

print(EditDist(A,B))
                


    
