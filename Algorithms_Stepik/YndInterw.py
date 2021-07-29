
A = [[-2,5],[-3,3],[2,3],[-4,4],[1,5],[3,4],[-2,0],[1,0],[-2,5],[1,5]] # n float points [x,y]

n = len(A)

Levels = {}
Ys = []

for i in range(n):
    if A[i][1] in Levels:
        Levels[A[i][1]].append(A[i][0])
    else:
        Levels[A[i][1]] = [A[i][0]]
        Ys.append(A[i][1])

prevAvg = 0
i = 0
f = False
for y in Ys:
    level = sorted(Levels[y])
    nL = len(level)
    avgL = sum(level)/nL
    if i > 0 and avgL != prevAvg:
        print("NO")
        f = True
        break
    else:    
        L = 0
        R = nL - 1
        while L < R:
            if level[L] + level[R] == 2*avgL:
                L += 1
                R -= 1
            else:
                print("NO")
                f = True
                break
    if f:
        break               

    prevAvg = avgL
    i += 1

if not f:
    print("YES")







    
        
