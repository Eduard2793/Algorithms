
n = int(input())
arr = list(map(int,input().split()))

c = [0]
for a in arr:
    nc = len(c)
    if a >= nc:
        for i in range(nc,a+1):
            c.append(0)
        c[a] += 1
    else:
        c[a] += 1

arrN = []
for i in range(len(c)):
    for j in range(c[i]):
        arrN.append(i)

print(*arrN)
