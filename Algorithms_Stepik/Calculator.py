
n = int(input())

D = [-1]*(n+1)
D[0] = -4
D[1] = 0

Dprevs = [0]*(n+1)
Dprevs[1] = 0

for i in range(2,n+1):
    if i%2 == 0:
        if i%3 == 0:
            D[i] = min(D[i//2], D[i//3], D[i-1]) + 1
        else:
            D[i] = min(D[i//2], D[i-1]) + 1
    else:
        if i%3 == 0:
            D[i] = min(D[i//3], D[i-1]) + 1
        else:
            D[i] = D[i-1] + 1
    
    if i%3 == 0 and D[i] == D[i//3] + 1:
        Dprevs[i] = i//3
    elif i%2 == 0 and D[i] == D[i//2] + 1:
        Dprevs[i] = i//2
    elif D[i] == D[i-1] + 1:
        Dprevs[i] = i-1
    else:
        print("Fuck!")

Sequence = [n]
i = n
while i > 1:
    i = Dprevs[i]
    Sequence.insert(0,i)

print(D[n])
print(*Sequence)
    

    
