
pas = []
stack = []
W = []

(N,M) = map(int,input().split()) # вершины и ребра
nu = list(map(int,input().split()))

G = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    (a,b) = map(int,input().split())
    if nu[a-1] == nu[b-1]:
        G[a][b] = 1 # смежны но вес = 0
        G[b][a] = 1
    else:
        G[a][b] = 2 # смежны и вес = 1 разные бароны
        G[b][a] = 2

def find_pas(v,G):
    if v == N:
        pas.append(v)
        print(sum(W),end=' ')
        print(len(pas))
        print(*pas)
        return
    else:
        w_two = 0
        neht = 0
        for w in range(1,N+1):
            if G[v][w] == 1:
                G[v][w] = 0
                G[w][v] = 0
                neht = w
                break
            if G[v][w] == 2:
                w_two = w
                
        if neht == 0:
            if w_two == 0:
                if len(pas) == 0:
                    print("impossible")
                    return
                else:
                    neht = pas.pop()
                    W.pop()
            else:
                G[v][w_two] = 0
                G[w_two][v] = 0
                neht = w_two
                if v%2 == 0:
                    W.append(2)
                else:
                    W.append(1)
                pas.append(v)
        else:
            W.append(0)
            pas.append(v)
        find_pas(neht,G)

find_pas(1,G)
        
                
                
                
                
        
        
    


