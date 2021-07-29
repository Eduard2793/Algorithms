
n = int(input())
E = [[] for _ in range(n+1)]
w = [0]*(n+1)
f = [0]*(n+1)
g = [0]*(n+1)
for i in range(1,n+1):
    (p,q) = (map(int,input().split()))
    E[p].append(i)
    w[i] = q

def DFS(v):
    global f, g, w, E
    f[v] = w[v]
    g[v] = 0
    for kid in E[v]:
        DFS(kid)
    for kid in E[v]:
        f[v] = f[v] + g[kid]
        g[v] = g[v] + max(g[kid],f[kid])

r = E[0][0]
DFS(r)
print(max(f[r],g[r]))
  
