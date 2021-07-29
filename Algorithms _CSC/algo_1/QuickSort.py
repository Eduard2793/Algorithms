
'''
n = int(input())
arr = list(map(int,input().split()))
n = len(arr)

def partition(arr,L,R):
    i = L
    for j in range(L,R-1):
        if arr[j] < arr[R-1]:
            ai = arr[i]
            arr[i] = arr[j]
            arr[j] = ai
            i += 1
    ai = arr[i]
    arr[i] = arr[R-1]
    arr[R-1] = ai
    return i

def quickSort(arr,L,R):
    if L < R-1:
        i = partition(arr,L,R)
        quickSort(arr,L,i)
        quickSort(arr,i+1,R)

quickSort(arr,0,n)

print(*arr)
    
'''

n = int(input())
A = list(map(int,input().split()))
n = len(A)

def partition(A,L,R,key):
    j1 = L
    j2 = L
    x = A[L]
    for i in range(L+1,R+1):
        if key(A[i]) < key(x):
            j1 += 1
            Ai = A[i]
            A[i] = A[j1]
            A[j1] = Ai
            
        elif key(A[i]) == key(x):
            j2 += 1
            Ai = A[i]
            A[i] = A[j2]
            A[j2] = Ai
        
    A[L] = A[j1]
    A[j1] = x
    j1 -= 1
    return [j1,j2]      

def mySort(A,L,R,key):
    if L < R:
        [j1,j2] = partition(A,L,R,key)
        mySort(A,L,j1,key)
        mySort(A,j2+1,R,key)

mySort(A,0,n-1,key = lambda x : x)

print(*A)












































