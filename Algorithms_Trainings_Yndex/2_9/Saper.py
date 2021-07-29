
[N,M,K] = map(int,input().split())

D = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(0)
    D.append(row)

for i in range(K):
    [x,y] = map(int,input().split())
    D[x-1][y-1] = -1

def countMins(i,j):
    global D
    neighbors = [[i-1, j-1], [i-1, j],
                 [i-1, j+1], [i, j-1],
                 [i, j+1], [i+1, j-1],
                 [i+1, j], [i+1, j+1]]
    G = 0
    for i in range(8):
        if neighbors[i][0] < 0 or neighbors[i][0] >= N or neighbors[i][1] < 0 or neighbors[i][1] >= M:
            G += 0
        elif D[neighbors[i][0]][neighbors[i][1]] == -1:
            G += 1
        
    return G

for i in range(N):
    for j in range(M):
        if D[i][j] != -1:
            G = countMins(i,j)
            D[i][j] = G

for i in range(N):
    for j in range(M):
        G = D[i][j]
        if G != -1:
            print(G,end=' ')
        else:
            print('*',end=' ')
    print()
        
