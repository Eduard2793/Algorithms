
P = input()
S = input()

if P == '':
    if S == '':
        print("YES")
    else:
        print("NO")
elif S == '':
    if P == '*'*len(P):
        print("YES")
    else:
        print("NO")
else:      
    p = len(P)
    s = len(S)

    f = []
    for i in range(p):
        st = []
        for j in range(s):
            st.append(False)
        f.append(st)
        
    star = 0
    for i in range(0,p):
        if P[i] == '*':
            star += 1
        for j in range(0,s):
            if i > 0 and j > 0:
                if P[i] == '*':
                    f[i][j] = f[i-1][j] or f[i-1][j-1] or f[i][j-1]
                elif P[i] == '?':
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = f[i-1][j-1] and P[i] == S[j]
            elif i == 0:
                if j == 0:
                    f[0][0] = (P[0] == '*') or (P[0] == '?') or (P[0] == S[0])
                else:
                    f[0][j] = (P[0] == '*')
            else:
                if f[i-1][0] == False:
                    f[i][0] = False
                else:
                    if P[i] == '*':
                        f[i][0] = True
                    else:
                        if star != i:
                            f[i][0] = False
                        else:
                            if P[i] == S[0] or P[i] == '?' or P[i] == '*':
                                f[i][0] = True  

    if f[p-1][s-1] == True:
        print("YES")
    else:
        print("NO")

        
