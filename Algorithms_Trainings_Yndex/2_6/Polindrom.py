
n = int(input())
A = list(map(int, input().split()))


f = False

for LL in range(n):
    R = n-1
    L = LL
    while True:
        if A[R] == A[L]:
            if R == L + 2 or R == L + 1 or R == L:
                f = True
                break
            R -= 1
            L += 1
        else:
            break
    if f:
        break

j = LL-1
ans = []
while j >= 0:
    ans.append(A[j])
    j -= 1

print(len(ans))
if len(ans) != 0:
    print(*ans)

            
