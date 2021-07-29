
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
res = []
for i in range(k):
    (a,b) = map(int,input().split())
    r = 0
    for j in range(n):
        if arr[j] > b:
            break
        
        elif arr[j] >= a: # and arr[j] <= b:
            r += 1
            
    res.append(r)

for p in range(k):
    print(res[p],end='')
    print(" ",end='')
    
