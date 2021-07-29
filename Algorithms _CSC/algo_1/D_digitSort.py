
def sortMS_by_k(MS,k):
    c = [0]
    for S in MS:
        nc = len(c)
        a = S[k]
        if a >= nc:
            for i in range(nc,a+1):
                c.append(0)
            c[a] += 1
        else:
            c[a] += 1

    M = len(c) - 1
    h = [0]
    for i in range(1,M+1):
        h.append(h[i-1] + c[i-1])
        
    MSsort = [0]*len(MS)
    for i in range(len(MS)):
        MSsort[h[MS[i][k]]] = MS[i]
        h[MS[i][k]] += 1

    return MSsort

def Sort_K_time(MS,K,m):
    for k in range(K):
        MS = sortMS_by_k(MS,m-k-1)
    return MS
        

a = list(map(int, input().split()))
n = a[0] # quantity
m = a[1] # length
K = a[2] # fase

MS = []
for i in range(n):
    s = input()
    arrS = []
    for j in range(m):
        arrS.append(ord(s[j]))

    MS.append(arrS)

MSsort = Sort_K_time(MS,K,m)

for i in range(n):
    for j in range(m):
        print(chr(MSsort[i][j]),end='')
    print()




    
    
