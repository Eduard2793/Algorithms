
nA = list(map(int,input().split()))
kB = list(map(int,input().split()))

def binarySearch(b):
    global nA
    l = 1
    r = nA[0]
    while l <= r:
        m = l + (r-l)//2

        if nA[m] == b:
            return m

        elif nA[m] > b:
            r = m-1

        else:
            l = m+1
    return -1

for i in range(1,kB[0]+1):
    print(binarySearch(kB[i]),end=' ')


