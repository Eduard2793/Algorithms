
n = int(input())
A = list(map(int,input().split()))

if n == 1:
    print(A[0])
elif n == 2:
    print(max(A[0]+A[1],A[1]))
else:
    D = [A[0],max(A[0]+A[1],A[1])]

    for i in range(2,n):
        D.append(max((D[i-1]+A[i]),(D[i-2]+A[i])))

    print(D[n-1])
