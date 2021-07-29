
C = float(input())

a = 0
b = C

for i in range(10**6):
    x = (a + b)/2
    res = x**2 + x**0.5
    if abs(C - res) < 0.000001:
        print(x)
        break
    elif res < C:
        a = x
    else:
        b = x

