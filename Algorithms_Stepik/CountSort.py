
n = int(input()) # <= 10^4
A = list(map(int,input().split())) # A[i] <= 10

def countSort(A,n):
    A_ = [0]*n
    M = 11
    B = [0]*M
    for j in range(n):
        B[A[j]] += 1
    for i in range(1,M):
        B[i] = B[i] + B[i-1] # в В записано сколько раз встречается но не индекс
        # индекс на 1 меньше
    for j in range(1,n+1):
        A_[B[A[-j]]-1] = A[-j] 
        B[A[-j]] -= 1
        
    return A_

print(*countSort(A,n))
