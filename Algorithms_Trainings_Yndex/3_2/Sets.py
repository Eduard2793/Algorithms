
A = list(map(int, input().split()))
B = list(map(int, input().split()))

D = [0]*(max(max(A),max(B))+1)

n = len(A)
m = len(B)

for i in range(n):
    D[A[i]] = 1


for i in range(m):
    if D[B[i]] == 1:
        D[B[i]] = 2

for i in range(len(D)):
    if D[i] == 2:
        print(i,end=" ")
        
        
    
    
