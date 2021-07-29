ve = input().split(" ")
v = int(ve[0])
e = int(ve[1])

def Graf():
    graf = True
    if e <= 0 or v <= 1:
        graf = False
    return graf


graf = Graf()

if graf:
    Pas = []
    vers = []
    for i in range(0,e):
        reb = input().split(" ")
        x = int(reb[0])
        y = int(reb[1])
        if x > v or y > v or x == y:
            graf = False
            break
        else:
            Pas.append([x,y])
            if x not in vers:
                vers.append(x)
            if y not in vers:
                vers.append(y)
    
if graf:
    stuff = True
    t = len(Pas)
    while stuff:
        flag = False
        n = len(Pas)
        for i in range(n):
            if flag:
                break
            else:
                for j in range(0,len(Pas[i])):
                    if flag:
                        break
                    else:
                        for p in Pas:
                            if flag:
                                break
                            else:
                                if p != Pas[i]:
                                    if Pas[i][j] in p:
                                        Pas[i].extend(p)
                                        Pas.remove(p)
                                        t = len(Pas)
                                        flag = True
        if n == t:
            stuff = False

         
    w = v - len(vers)
    print(len(Pas) + w)
else:
    if e == 0:
        print(v)
    else:
        print(0)
























