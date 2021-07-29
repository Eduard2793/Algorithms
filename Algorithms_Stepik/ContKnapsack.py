
[n, W] = map(int, input().split())
things = []
for i in range(n):
    [c, w] = map(int, input().split())
    things.append([c,w,c/w])
    
sort = sorted(things, key = lambda x : -x[2])
totC = 0
#totW = 0
for i in range(n):
    c = sort[i][0]
    w = sort[i][1]
    if W//w != 0: # значит предмет помещается полностью в рюкзак
        totC += c
        #totW += w
        W -= w
    else:
        totC += (W/w)*c
        #totW += (W/w)*w
        W = 0
        break
    
print(totC)   
        
