
hip = ['0']
p = 0
P = ['0']

def siftUp(i):
    global hip, P
    while i > 1 and hip[i][0] < hip[int(i/2)][0]:
        #=========
        P[hip[i][1]] = int(i/2)
        P[hip[int(i/2)][1]] = i
        a = hip[i]
        hip[i] = hip[int(i/2)]
        hip[int(i/2)] = a
        #=========
        i = int(i/2)
    return i # куда он попал

def siftDown(i):
    global hip, P
    n = len(hip)-1
    while 2*i <= n:
        j = 2*i
        if 2*i + 1 <= n and hip[j][0] > hip[2*i+1][0]:
            j = 2*i + 1
        if hip[i][0] <= hip[j][0]:
            break
        #=========
        P[hip[i][1]] = j
        P[hip[j][1]] = i
        a = hip[i]
        hip[i] = hip[j]
        hip[j] = a
        #=========
        i = j

def insert(x):
    global hip, p, P
    p += 1
    hip.append([x,p])
    P.append(len(hip)-1) # P[p] == номер в куче элемента с идентификатором p
    siftUp(len(hip)-1)

def extractMin():
    global hip
    if len(hip) == 1:
        m = '*'
    elif len(hip) > 1:
        m = hip[1]
        #=========
        n = len(hip)-1
        P[hip[1][1]] = n
        a = hip[n]
        P[a[1]] = 1
        hip[1] = a
        #=========
        hip.pop()
        siftDown(1)
    else:
        m = "jjkn"
        
    return m

def decreaseKey(i,x):
    global hip, P, p
    p += 1
    if P[i] <= len(hip)-1:
        hip[P[i]][0] = min(hip[P[i]][0],x)
        siftUp(P[i])

while True:
    try:
        r = input()
    except (Exception):
        break
    opr = r.split()
    if opr[0] == "push":
        insert(int(opr[1]))
    if opr[0] == "extract-min":
        print(*extractMin())
    if opr[0] == "decrease-key":
        decreaseKey(int(opr[1]),int(opr[2]))




















        


