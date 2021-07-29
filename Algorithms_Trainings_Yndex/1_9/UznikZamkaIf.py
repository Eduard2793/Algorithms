
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def chekRectAngle(w,h):
    global D, E
    if w <= D and h <= E or w <= E and h <= D:
        return True
    else:
        return False

if chekRectAngle(A,B) or chekRectAngle(A,C) or chekRectAngle(B,C):
    print("YES")
else:
    print("NO")
