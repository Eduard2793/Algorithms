
n = int(input())
a = list(map(int,input().split()))
f = [1]*n
g = [-1]*n
fm = 1
fmj = 0
for j in range(1,n):
    for i in range(j):
        if a[i] < a[j] and f[j] <= f[i]:
            f[j] = f[i] + 1
            g[j] = i # индекс предпоследнего
            if fm < f[j]:
                fm = f[j]
                fmj = j
r = []
resN = 0
while fmj > -1:
    r.append(a[fmj])
    resN += 1
    fmj = g[fmj]

print(fm)
for i in range(1,resN+1):
    print(r[-i],end=' ')
