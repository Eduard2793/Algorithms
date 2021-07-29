
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

f = []
def trevel(a,n):
    inf = 6666666666
    global f
    for i in range(2**n):
        s = []
        for v in range(n):
            if i == 2**v:
                s.append(0)
            else:
                s.append(inf)
        f.append(s)
    for A in range(1,2**n):
        if (A & (A-1)) != 0:
            for v in range(n):
                if (A & 2**v) != 0:
                    for u in range(n):
                        if (A & 2**u != 0) and u != v:
                            f[A][v] = min(f[A][v],f[A & (~ 2**v)][u] + a[u][v])                        
                            
    return min(f[2**n - 1])

S = trevel(a,n)
s = S
path = []
A = 2**n - 1
path.append([s,f[A].index(s)])
while A != 0:
    m = len(path)-1
    A = A & (~ 2**path[m][1])
    for v in range(n):
        if f[A][v] + a[v][path[m][1]] == path[m][0]:
            path.append([f[A][v],v])
            break

path_ = []
i = n-1
while i >= 0:
    path_.append(path[i][1]+1)
    i -= 1

print(S)
print(*path_)

