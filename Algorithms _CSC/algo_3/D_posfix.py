
stack = []
vr = input().split()
for i in range(len(vr)):
    s = vr[i]
    if s == '+':
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)
    elif s == '-':
        x = stack.pop()
        y = stack.pop()
        stack.append(y-x)
    elif s == '*':
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)
    else:
        stack.append(int(s))

print(*stack)
        
    
