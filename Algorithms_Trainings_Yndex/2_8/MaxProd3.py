
A = list(map(int, input().split()))
n = len(A)
Max = [A[0], 0]

for i in range(n):
    if A[i] > Max[0]:
        Max = [A[i], i]

if Max[1] != 0:
    Max2 = [A[0], 0]
else:
    Max2 = [A[1], 1]

for i in range(n):
    if A[i] > Max2[0] and i != Max[1]:
        Max2 = [A[i], i]

Min = [A[0], 0]

for i in range(n):
    if A[i] < Min[0]:
        Min = [A[i], i]

if Min[1] != 0:
    Min2 = [A[0], 0]
else:
    Min2 = [A[1], 1]

for i in range(n):
    if A[i] < Min2[0] and i != Min[1]:
        Min2 = [A[i], i]

third1 = min(A)-1
for i in range(n):
    if i != Max[1] and i != Max2[1] and A[i] > third1:
        third1 = A[i]

third2 = min(A)-1
for i in range(n):
    if i != Min[1] and i != Min2[1] and A[i] > third2:
        third2 = A[i]

if Max[0]*Max2[0]*third1 >= Min[0]*Min2[0]*third2:            
    print(*[Max2[0], Max[0], third1])
else:        
    print(*[Min[0], Min2[0], third2])

    
