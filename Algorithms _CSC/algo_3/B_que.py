
arr = []
had = 0
m = int(input())
for i in range(m):
    op = input().split()
    if len(op) == 1:
        print(arr[had])
        had += 1
    else:
        el = int(op[1])
        arr.append(el)
