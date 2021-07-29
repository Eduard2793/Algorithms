
a = int(input())
b = int(input())
n = int(input())
m = int(input())

Min1 = (n-1)*(a+1) + 1 
Min2 = (m-1)*(b+1) + 1

Max1 = Min1 + 2*a
Max2 = Min2 + 2*b

Tmin = max(Min1,Min2)
Tmax = min(Max1,Max2)

if Tmax > Tmin:
    print(str(Tmin) + " " + str(Tmax))
else:
    print(-1)
