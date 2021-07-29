
n = int(input())

K = int(((1+16*n)**0.5 - 1)/2)
#print(K)
augend = [0]*(K+1)
augend[1] = 1
i = 1
s = 1
#print(1, end=" ")
while True:
    if s > n:
        augend[s-n] = 0
        i -= 1
        s = n
        #print("*" + str(s-n) + "*", end=" ")
        break
    elif s == n:
        break
    else:
        i += 1
        augend[i] = 1
        #print(i, end=" ")
        s += i

print(i)
f = 0
for j in range(K+1):
    if augend[j] == 1:
        print(j, end=" ")
        f += 1
    if f == i:
        break

