'''

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

k = len(code)

if len(code) == 1:
    l = len(s)
    code = [[s[0],"0"]]
    code_s = "0"*len(s)

else:
    
    codeWord = ""

    for ch in s:
        for i in range(len(code)):
            if ch == code[i][0]:
                codeWord += code[i][1]
                break
            
    l = len(codeWord)

    sort_cod = sorted(code, key = lambda x : x[0])
    code = sort_cod.copy()

    code_s = codeWord



'''
import sys

[k, l] = map(int, sys.stdin.readline().split())
code = []
for i in range(k):
    st = sys.stdin.readline().split("\n")
    st = st[0].split(": ") 
    code.append([st[0],st[1]])
    
code_s = sys.stdin.readline()

class B_Node():
    def __init__(self, lable, ch, kid_L, kid_R):
        self.lable = lable
        self.ch = ch
        self.kid_L = kid_L
        self.kid_R = kid_R
        self.visited = False

def go_to_leaf_and_create_Nodes(Node, ch, code_of_ch, deep):
    if len(code_of_ch) == 1:
        if code_of_ch[0] == "0":
            Node.kid_L = B_Node(deep, ch, None, None)
            
        if code_of_ch[0] == "1":
            Node.kid_R = B_Node(deep, ch, None, None)
        return
    
    else: # >= 2
        bit = code_of_ch[0]
        code_of_ch_minus_first = ""
        for i in range(1,len(code_of_ch)):
            code_of_ch_minus_first += code_of_ch[i]

        if bit == "0":
            if Node.kid_L == None:
                Node.kid_L = B_Node(None, None, None, None)
            go_to_leaf_and_create_Nodes(Node.kid_L, ch, code_of_ch_minus_first, deep+1)
            
        if bit == "1":
            if Node.kid_R == None:
                Node.kid_R = B_Node(None, None, None, None)
            go_to_leaf_and_create_Nodes(Node.kid_R, ch, code_of_ch_minus_first, deep+1)
    
   
def BuildTree(code):
    root = B_Node(None, None, None, None)
    for i in range(len(code)):
        ch_cod = code[i]
        go_to_leaf_and_create_Nodes(root, ch_cod[0], ch_cod[1], 0)

    return root

s = ""
d = 0
def go_to_leaf_and_get_ch(Node,code_s):
    global s, d
    if Node.kid_L == None and Node.kid_R == None:
        s += Node.ch
        d = Node.lable+1
        return
    else:
        bit = code_s[0]
        code_s_minus_first = ""
        for i in range(1,len(code_s)):
            code_s_minus_first += code_s[i]

        if bit == "0":
            go_to_leaf_and_get_ch(Node.kid_L, code_s_minus_first)
        if bit == "1":
            go_to_leaf_and_get_ch(Node.kid_R, code_s_minus_first)    

Tree = BuildTree(code)

t = 0
while code_s != '':
    if t > l:
        print(l)
        break
    else:
        go_to_leaf_and_get_ch(Tree, code_s)
        code_s_minus_first_d = ''
        for i in range(d,len(code_s)):
            code_s_minus_first_d += code_s[i]
        code_s = code_s_minus_first_d
        t+=1
        
     
print(s)  

