
[troom, tcond] = map(int, input().split())
regim = input()

def countT(troom, tcond, regim):
    if regim == 'freeze':
        return min(troom, tcond)
    elif regim == 'heat':
        return max(troom, tcond)
    elif regim == 'auto':
        return tcond
    elif regim == 'fan':
        return troom
    else:
        print("Fuck!")

print(countT(troom, tcond, regim))
