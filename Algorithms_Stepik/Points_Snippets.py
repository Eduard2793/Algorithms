
n = int(input())
otrezki = []
for i in range(n):
    [l, r] = map(int, input().split())
    otrezki.append([l, r])

sort = sorted(otrezki, key = lambda x : x[1])
points = []
points.append(sort[0][1])
for i in range(1,n):
    if sort[i][0] > points[-1]: # то не он покрыт
        points.append(sort[i][1])

print(len(points))
print(*points)
