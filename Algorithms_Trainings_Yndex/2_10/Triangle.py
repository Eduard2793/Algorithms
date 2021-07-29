

n = int(input())
prev = float(input())
L = 30.0
R = 4000.0
for i in range(n-1):
    [noteS, prox] = input().split()
    note = float(noteS)
    if abs(note - prev) < 10**(-6):
        continue
    if prox == 'closer':
        if note > prev:
            L = max(L, (prev+note)/2)
        else:
            R = min(R, (prev+note)/2)
    else:
        if note > prev:
            R = min(R, (prev+note)/2)
        else:
            L = max(L, (prev+note)/2)
    
    prev = note
                
print(*[L,R])
