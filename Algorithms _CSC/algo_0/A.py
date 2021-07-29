
def find_triple(arr):
    n = len(arr)
    arr_new = []
    end_of_same = n
    same = 0
    for i in range(n):
        ai = arr[i]
        same = 1
        for j in range(i+1,n):
            aj = arr[j]
            if ai != aj:
                break
            else:
                same += 1
        if same >= 3:
            end_of_same = i + same
            break
        else:
            arr_new.append(ai)
            
    for k in range(end_of_same,n):
        arr_new.append(arr[k])

    return (same,arr_new)

SAME = 0

def foo(arr):
    global SAME
    res = find_triple(arr)
    same = res[0]
    arr_new = res[1]
    if same < 3:
        return SAME
    else:
        SAME += same
        return foo(arr_new)

arr = list(map(int,input().split()))
print(foo(arr))

