
N = int(input())

A = [[0] * 10 for _ in range(N+1)]
# A[q][p] = число q-значных чисел начинающихся с p

for q in range(1,N+1):
    for p in range(0,10):
        if q == 1:
            A[q][p] = 1
        else:
            if p == 0:
                A[q][p] = A[q-1][p] + A[q-1][p+1]
            elif p == 9:
                A[q][p] = A[q-1][p] + A[q-1][p-1]
            else:
                A[q][p] = A[q-1][p-1] + A[q-1][p] + A[q-1][p+1]

a = A[N]
print(sum(a) - a[0])
