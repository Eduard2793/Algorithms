
def merge(A,B,key):
    C = []
    i = 0
    j = 0
    while True:
        
        if key(A[i]) <= key(B[j]):
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
        if i == len(A):
            for k in range(j,len(B)):
                C.append(B[k])
            break
        if j == len(B):
            for k in range(i,len(A)):
                C.append(A[k])
            break
    return C
    
    
def mySort(arr,key):
    if len(arr) > 1:
        m = len(arr) // 2
        return merge(mySort(arr[0:m],key), mySort(arr[m:],key),key)
    else:
        return arr
    
    #return sorted(A,key=key)

def binSearch(point,Asorted,key):
    n = len(Asorted)
    k = 0
    l = 0
    r = n-1
    if key == "L":
        while l <= r:
            m = l + (r-l)//2
            if Asorted[m][0] <= point:
                # все более левые могут включать точку
                k += (m+1-l)
                l = m+1
                # идем смотреть правую часть
            else:
                # этот и более правые отрезки начинаются правее точки
                r = m-1
                # идем смотреть левую часть
                
    if key == "R":
        while l <= r:
            m = l + (r-l)//2
            if Asorted[m][1] < point:
                # все более левые правые границы левее точки
                k += (m+1-l)
                l = m+1
                # идем смотреть правую часть (может там тоже есть что то левее точки)
            else:
                # значит более правые отрезки и этот могут включать точку
                # они не нужны
                r = m-1
                # идем смотреть левую часть
    return k


[n,m] = map(int, input().split())
cutsLsort = []
cutsRsort = []
for i in range(n):
    [a,b] = map(int, input().split())
    cutsLsort.append([a,b])
    cutsRsort.append([a,b])

points = list(map(int, input().split()))

Lsort = mySort(cutsLsort, key = lambda x : x[0])
Rsort = mySort(cutsRsort, key = lambda x : x[1])

def countCuts(point):
    global Lsort, Rsort

    lam = binSearch(point,Lsort,"L")
    if lam == 0: # маленькая оптимизация, но и так ro будет равен 0
        return 0
    else:
        ro = binSearch(point,Rsort,"R")
        return lam-ro

Ans = []
for point in points:
    ans = countCuts(point)
    Ans.append(ans)
print(*Ans)

