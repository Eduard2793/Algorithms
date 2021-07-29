
[w1, h1, w2, h2] = map(int, input().split())

A = [(w1+w2)*max(h1,h2)]
B = [[(w1+w2),max(h1,h2)]]

A.append(max(h1,h2)*(w1+w2))
B.append([max(h1,h2),(w1+w2)])

A.append((w1+h2)*max(h1,w2))
B.append([(w1+h2),max(h1,w2)])

A.append(max(h1,w2)*(w1+h2))
B.append([max(h1,w2),(w1+h2)])

A.append((h1+w2)*max(w1,h2))
B.append([(h1+w2),max(w1,h2)])

A.append(max(w1,h2)*(h1+w2))
B.append([max(w1,h2),(h1+w2)])

A.append((h1+h2)*max(w1,w2))
B.append([(h1+h2),max(w1,w2)])

A.append(max(w1,w2)*(h1+h2))
B.append([max(w1,w2),(h1+h2)])

s = min(A)
for i in range(8):
    if A[i] == s:
        print(*B[i])
        break
    
    
    
