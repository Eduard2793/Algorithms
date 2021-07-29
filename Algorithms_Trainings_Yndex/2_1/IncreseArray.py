
A = list(map(int,input().split()))
n = len(A)
k = 0
for i in range(1,n):
    d = A[i] - A[i-1]
    if d > 0:
        k += 1

if k == n-1:
    print("YES")
else:
    print("NO")

