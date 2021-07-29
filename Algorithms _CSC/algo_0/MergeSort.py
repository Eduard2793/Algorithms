def foo(a,b):
    res = []
    for i in range(0,len(a)):
        res.append(a[i])
        
    for i in range(0,len(b)):
        res.append(b[i])

    return res


def merge(a,b): # два отсортированных массива
    res = []
    n = len(a) + len(b)
    i = 0
    for i in range(n):
        if a[i] <= b[i]:
            temp_big2 = b[i]
            if a[i] <= temp_big1:
                res.append(a[i])
                temp_big2 = b[i]
            else:
                res.append(temp_big1)
                res.append(a[i])
                temp_big1 = b[i]
            
            
    for i in range(n,len(a)):
        res.append(a[i])
        
    for i in range(n,len(b)):
        res.append(b[i])

    return res

a = [21, 23, 24, 40, 75, 76, 78, 77, 900, 2100, 2200, 2300, 2400, 2500]
b = [10, 11, 41, 50, 65, 86, 98, 101, 190, 1100, 1200, 3000, 5000]

q = sorted(foo(a,b))
e = merge(a,b)

print(q)
print(e)
