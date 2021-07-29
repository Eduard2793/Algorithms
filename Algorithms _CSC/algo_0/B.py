
N = int(input())

F = [0]*(N+1)

prevs = [0]*(N+1)

res = [N]

for i in range(2,N+1):
    F[i] = F[i - 1]
    prev = i-1
    
    if i%2 == 0 and F[i//2] < F[i]:
        F[i] = F[i//2]
        prev = i//2
        
    if i%3 == 0 and F[i//3] < F[i]:
        F[i] = F[i//3]
        prev = i//3
        
    F[i] += 1
    prevs[i] = prev # => на i-ом месте стоит то что было до числа i
# таким образом можно восстановить последовательность как это делается ниже

i = N
while prevs[i] > 0:
    res.append(prevs[i])
    i = prevs[i]

print(F[N])
print(*res[::-1])
