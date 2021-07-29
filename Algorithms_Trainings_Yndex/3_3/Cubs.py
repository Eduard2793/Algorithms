
[N, M] = map(int,input().split())

A = []
for i in range(N):
    A.append(int(input()))

B = []
for i in range(M):
    B.append(int(input()))

As = set(A)
Bs = set(B)

P = []
B_A = []
for i in range(M):
    if B[i] in As:
        P.append(B[i])
    else:
        B_A.append(B[i])

A_B = []
for i in range(N):
    if A[i] not in Bs:
        A_B.append(A[i])

print(len(P))
print(*sorted(P))
print(len(A_B))
print(*sorted(A_B))
print(len(B_A))
print(*sorted(B_A))
        
'''
if len(A) != 0 and len(B) != 0:
    Max = max(max(A),max(B))
elif len(A) != 0:
    Max = max(A)
elif len(B) != 0:
    Max = max(B)
else:
    Max = -1    

D = [0]*(Max+1)

for i in range(N):
    D[A[i]] = 1

P = []
B_A = []

for i in range(M):
    if D[B[i]] == 1:
        P.append(B[i])
        D[B[i]] = 2
    else:
        B_A.append(B[i])

A_B = []
for i in range(N):
    if D[A[i]] == 1:
        A_B.append(A[i])

print(len(P))
print(*sorted(P))
print(len(A_B))
print(*sorted(A_B))
print(len(B_A))
print(*sorted(B_A))
'''



        
        

    
    
