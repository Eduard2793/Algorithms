
#Pupils = []

Union = set()
Intersection = dict()

N = int(input()) # pupils
for i in range(N):
    M = int(input()) # lenguages
    #Lenguages = []
    for j in range(M):
        leng = input()
        #Lenguages.append(leng)
        Union.add(leng)
        if leng not in Intersection:
            Intersection[leng] = 1
        else:
            Intersection[leng] += 1
    
    #Pupils.append(Lenguages)
            
lenguages = Intersection.keys()
I = []

for leng in lenguages:
    if Intersection[leng] == N:
        I.append(leng)

print(len(I))
for i in range(len(I)):
    print(I[i])

print(len(Union))
U = list(Union)
for i in range(len(Union)):
    print(U[i])
    




