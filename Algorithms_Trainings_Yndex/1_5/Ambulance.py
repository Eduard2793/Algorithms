
[K1, M, K2, P2, N2] = map(int,input().split())

Z2 = (P2-1)*M + N2

if Z2 == 1:
    if M == 1:
        if K2 == K1:
            print("1 1")
        else:
            print("0 1")
    else:
        print("-1 -1")
else:
    j = 0
    for x in range(1,K2//(Z2)+1):
        if Z2*x - K2 == (Z2*x) % K2: #(K2-1)//x + 1 == Z2:
            j += 1
            print(x,end=' ')
    if j < 1:
        pass
    elif j > 1:
        pass
    else:
        Z1 = (K1-1)//x + 1
        P1 = Z1//M + 1
        N1 = Z1%((P1-1)*M)
        print(str(P1) + " " + str(N1))
        

