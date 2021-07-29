# http://fpmi-bsu.narod.ru/author/Heap/Help/d_feat.html
# http://fpmi-bsu.narod.ru/author/Heap/Help/d_act.html

import sys

class Hip():
    def __init__(self): # Max hip => first is the maximum
        self.arr = []
        return

    def siftUp(self,i):
        if i != 0 and self.arr[i] > self.arr[(i-1)//2]: # нарушен инвариант макс кучи
            per = self.arr[(i-1)//2]
            kid = self.arr[i]
            self.arr[i] = per
            self.arr[(i-1)//2] = kid
            self.siftUp((i-1)//2)
        return

    def siftDown(self,i):
        if 2*i+2 > len(self.arr)-1:
            if 2*i+1 > len(self.arr)-1:
                return
            else: # 2*i+1 == len(self.arr)-1
                if self.arr[i] < self.arr[2*i+1]:
                    kid = self.arr[2*i+1]
                    per = self.arr[i]
                    self.arr[i] = kid
                    self.arr[2*i+1] = per
                return
        elif self.arr[i] < max(self.arr[2*i+1], self.arr[2*i+2]):
            if self.arr[2*i+1] > self.arr[2*i+2]:
                max_i = 2*i+1
            else:
                max_i = 2*i+2
            kid = self.arr[max_i]
            per = self.arr[i]
            self.arr[i] = kid
            self.arr[max_i] = per
            self.siftDown(max_i)
            return
        else:
            return

    def Insert(self,p):
        self.arr.append(p)
        self.siftUp(len(self.arr)-1)
        return

    def ExtractMax(self): # is not empty
        if len(self.arr) == 0:
            return None
        elif len(self.arr) == 1:
            return self.arr.pop()
        elif len(self.arr) == 2:
            Max = self.arr[0]
            self.arr[0] = self.arr[1]
            self.arr.pop()
            return Max
        else:
            Max = self.arr[0]
            self.arr[0] = self.arr[len(self.arr)-1]
            self.arr.pop()
            self.siftDown(0)
            return Max


hip = Hip()

n = int(sys.stdin.readline())
for _ in range(n):
    st = sys.stdin.readline()
    op = st.split()
    typ = op[0]
    if typ == "Insert":
        hip.Insert(int(op[1]))
    if typ == "ExtractMax":
        print(hip.ExtractMax())


