
n = int(input())
arr = []
for i in range(n):
    op = input().split()
    if len(op) == 1:
        print(arr.pop())
    else:
        arr.append(op[1])
