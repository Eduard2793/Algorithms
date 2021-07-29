
S = input()

A = 0
AB = 0
ABC = 0
for let in S:
    if let == "a":
        A += 1
    if A != 0:
        if let == "b":
            AB += A
            
        if AB != 0:
            if let == "c":
                ABC += AB

print(ABC)      
