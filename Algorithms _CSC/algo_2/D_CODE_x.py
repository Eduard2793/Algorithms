
inf = 10**9 + 1        

N = int(input()) # 2 <= число символов в алфавите, то есть число листьев <= 300
a = list(map(int, input().split()))
#        f      p   k1  k2
tree = [[a[i], -1, -1, -1] for i in range(N)]

def serch_2_min_and_append_tree():
    n = len(a)
    global tree
    m1 = a[0]
    m1_i = 0
    for i in range(1,n):
        if m1 > a[i]:
            m1 = a[i]
            m1_i = i
    
    a[m1_i] = inf
    m2 = a[0]
    m2_i = 0
    for i in range(1,n):
        if m2 > a[i]:
            m2 = a[i]
            m2_i = i
    if m2 == inf:
        return 0
    else:
        a[m2_i] = inf

        a.append(m1+m2)
            
        tree[m1_i][1] = n
        tree[m2_i][1] = n    
        tree.append([m1+m2, -1, m1_i, m2_i])
        return 1  

res = 0
while True:
    res = serch_2_min_and_append_tree()
    if res == 0:
        break

T = len(tree)
print(tree)
def get_path_to_leav(root,path):
    pass

'''
pathes = []
for i in range(N):
    pathes.append(go_to_root(i))

print(*pathes)

'''
        
    











        
    
