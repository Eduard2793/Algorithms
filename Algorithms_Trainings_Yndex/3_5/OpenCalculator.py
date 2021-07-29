
import math as m

XYZ = list(map(int,input().split()))
N = int(input())

D = set()

Len = int(m.log(N,10)) + 1

for i in range(Len):
    d = N%10
    N = N//10
    if d not in XYZ:
        D.add(d)

print(len(D))
