
n = int(input())
arr = list(map(int, input().split()))
K = int(input())
Min = 10**9
Max = -10**9
quar = []
num = []
for k in range(K):
    (a,b) = input().split()
    [l,r] = (int(a),int(b))
    if Min > l:
        Min = l
    if Max < r:
        Max = r
    quar.append([l,r])
    num.append([0,0])

n_arr = []
for a in arr:
    if a <= Max and a >= Min:
        n_arr.append(a)


for na in n_arr:
    for k in range(K):
        if na <= quar[k][1]:
            num[k][1] += 1
        if na < quar[k][0]:
            num[k][0] += 1

for k in range(K):
    print((num[k][1] - num[k][0]),end=' ')

        
            
    
    
        



















'''
s = 0
    n2 = n//2
    for i in range(1,n2+1):
        left = arr[i-1]
        right = arr[-i]
        print(left,end=' ')
        print(right)
        if (left >= l and left <= r):
            s += 1
        if (right >= l and right <= r):
            s += 1
    if n%2 != 0:
        if (n2 >= l and n2 <= r):
            s += 1
    print(s,end=' ')
'''
