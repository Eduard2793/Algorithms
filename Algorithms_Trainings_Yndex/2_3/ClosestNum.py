
n = int(input())
A = list(map(int,input().split()))
x = int(input())

m = A[0]

for i in range(1,n):
    mn = A[i]
    if abs(mn - x) < abs(m - x):
        m = mn

print(m)
