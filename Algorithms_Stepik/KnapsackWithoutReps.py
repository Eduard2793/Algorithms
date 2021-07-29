
[W,n] = map(int,input().split())
wA = list(map(int,input().split()))

# costs == 1

def Knapsack(W,n,wA):
    D = []
    for i in range(W+1):
        row = []
        for j in range(n+1):
            row.append(0)
        D.append(row)
        
    for w in range(1,W+1):
        for i in range(1,n+1):
            D[w][i] = D[w][i-1]
            if wA[i-1] <= w:
                D[w][i] = max(D[w][i],D[w-wA[i-1]][i-1] + wA[i-1])    

    return D[W][n]

print(Knapsack(W,n,wA))
            
            
