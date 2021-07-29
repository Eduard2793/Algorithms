
a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif a == 0:
    if b == c**2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
elif (c**2 - b) % a == 0:
    print((c**2 - b) // a)
else:
    print("NO SOLUTION")
    
