
s = input()

se = sorted(list(set(s)))
F = [0]*len(se)

for i in range(len(se)):
    for ch in s:
        if ch == se[i]:
            F[i] += 1

class B_Node():
    def __init__(self, lable, ch, kid_L, kid_R):
        self.lable = lable
        self.ch = ch
        self.kid_L = kid_L
        self.kid_R = kid_R
        self.visited = False

class Hip():
    def __init__(self):
        self.arr = []

    def Insert(self, elem, key):
        self.arr.append(elem)
        self.arr = sorted(self.arr, key=key, reverse=True).copy()
        return 0

    def ExtractMin(self):
        return self.arr.pop()
#print(se)
#print(F)
def huffman(F):
    Tree = Hip()
    for i in range(len(F)):
        Tree.Insert(B_Node(F[i], se[i], None, None), key = lambda x : (x.lable, x.ch))
        
    for k in range(len(F)+1, 2*len(F)):
        M1 = Tree.ExtractMin()
        M2 = Tree.ExtractMin()
        #print(str(M1.lable) + "-" + M1.ch + "  " + str(M2.lable) + "-" + M2.ch)
        #print("----------------------")
        New = B_Node((M1.lable+M2.lable), (M1.ch+M2.ch), M1, M2) # слева всегда меньший
        Tree.Insert(New, key = lambda x : x.lable)

    return Tree

Tree = huffman(F).arr
root = Tree[0]

code = []

#Fsort = sorted(F, reverse=True)

def DVG(Node, c):
    #global code
    if Node.kid_L == None and Node.kid_R == None:
        code.append([Node.ch,c])
        Node.visited = True
        return
    else:
        if not Node.kid_L.visited:
            c += "0"
            DVG(Node.kid_L, c)
            #Node.kid_L.visited = True
            
        elif not Node.kid_R.visited:
            c += "1"
            DVG(Node.kid_R, c)
            #Node.kid_R.visited = True

        else:
            Node.visited = True
            return
        
while not root.visited:
    DVG(root, "")

print(len(code),end=' ')

if len(code) == 1:
    print(len(s))
    print(s[0] + ": " + str(0))
    print("0"*len(s))

else:
    
    codeWord = ""

    for ch in s:
        for i in range(len(code)):
            if ch == code[i][0]:
                codeWord += code[i][1]
                break
            
    print(len(codeWord))

    sort_cod = sorted(code, key = lambda x : x[0])

    for i in range(len(code)):
        ans = sort_cod[i][0] + ": " + sort_cod[i][1]
        print(ans)

    print(codeWord)








    
    
