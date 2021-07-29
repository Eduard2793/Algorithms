
S2 = input()
S1 = input()

D1 = {}

for i in range(len(S1)-1):
    pair = S1[i] + S1[i+1]
    if pair not in D1:
        D1[pair] = 1
    else:
        D1[pair] += 1

proxim = 0

for i in range(len(S2)-1):
    pair = S2[i] + S2[i+1]

    if pair in D1:
        proxim += 1

print(proxim)

