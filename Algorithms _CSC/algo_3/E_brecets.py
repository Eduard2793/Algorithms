
brecS = input()
stack = []
f = True
for b in brecS:
    
    if b == '(' or b == '[' or b == '{':
        stack.append(b)
    elif b == ')' or b == ']' or b == '}':
        if len(stack) == 0:
            print("NO")
            f = False
            break
        else:
            if b == ')' and stack[-1] == '(':
                stack.pop()
            elif b == ']' and stack[-1] == '[':
                stack.pop()
            elif b == '}' and stack[-1] == '{':
                stack.pop()
        
if f:
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
