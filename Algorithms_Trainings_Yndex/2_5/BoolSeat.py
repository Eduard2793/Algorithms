
n = int(input())
A = list(map(int,input().split()))

winer = max(A)

for i in range(n):
    if A[i] == winer:
        winer = [winer, i]
        break

vasia = -1

for i in range(winer[1]+1, n-1):
    if A[i]%10 == 5 and A[i+1] < A[i] and A[i] > vasia:
        vasia = A[i]

if vasia == -1:
    print(0)
else:
    k = 0
    for i in range(n):
        if A[i] > vasia:
            k += 1

    print(k+1)
        
        
