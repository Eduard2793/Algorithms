
n = int(input())
arr = []
arr2 = []
m = -1
for i in range(n):
    op = input().split()
    if len(op) == 1:
        if int(op[0]) == 2:
            if arr[len(arr)-1] == arr2[m]:
                arr2.pop()
                m -= 1
            arr.pop()
        else:
            print(arr2[m])
    else:
        arr.append(int(op[1]))
        if m == -1:
            arr2.append(int(op[1]))
            m += 1
        elif int(op[1]) <= arr2[m]:
            arr2.append(int(op[1]))
            m += 1
        
