
[N, K, M] = map(int, input().split())

totalNumOfDetails = 0

def useIntermediate(K):
    global M
    
    return [K//M, K%M]

def makeDetails(N):
    global totalNumOfDetails, K
    
    numOfIntermediates = N//K
    remainderFromInter = N%K
    
    [numOfDetails, remainderFromDetails] = useIntermediate(K)

    totalNumOfDetails += numOfIntermediates * numOfDetails

    remainder = remainderFromInter + numOfIntermediates * remainderFromDetails

    if remainder >= K:
        makeDetails(remainder)
    else:
        return

if M > K or K > N:
    print(0)
else:
    makeDetails(N)

    print(totalNumOfDetails)
        

