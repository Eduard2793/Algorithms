
N = 0

def merge(A,B):
    global N
    C = []
    i = 0
    j = 0
    while True:
        
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            N += (len(A) - i) # если i-ый элемент из левой части больше j-ого
            # из правой части, то и все остальные из левой части больше этого
            # j-ого элемента из правой (ведь А и В отсортированы) значит
            # на столько нужно увеличить количество инверсий
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
             
def sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        return merge( sort(arr[0:m]), sort(arr[m:]) )
    else:
        return arr
   
n = int(input())
arr = list(map(int,input().split()))

arr1 = sort(arr)
print(N)

