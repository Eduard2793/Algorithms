
n = int(input())
A = list(map(int,input().split()))

def lenLIS(A):
    D = [] # на позиции i стоит длина нвп заканчивающеся на элемент A[i]
    for i in range(len(A)):
        D.append(1)
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] >= D[i]:
                D[i] = D[j] + 1
    return max(D)

print(lenLIS(A))
                
    
