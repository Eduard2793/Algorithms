
A = list(map(int, input().split()))
k = 0
for i in range(1,len(A)-1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        k += 1

print(k)
    
    
