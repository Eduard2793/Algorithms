
def Comparator(n1,n2):
    i = 1
    j = 1
    k = 0
    while k < 7:
        ch1 = n1[-i]
        ch2 = n2[-j]

        if ch1 == '-':
            i += 1
            continue
        elif ch2 == '-':
            j += 1
            continue
        else:
            if int(ch1) == int(ch2):
                i += 1
                j += 1
                k += 1
            else:
                return False 
            
    if i-1 == len(n1):
        if j-1 == len(n2):
            return True
        else:
            #        nomer
            # _ code nomer
            k = 0
            i = 1
            while k < 3:
                ch1 = '495'[-i]
                ch2 = n2[-j]

                if ch1 == '-' or ch1 == ')' or ch1 == '(':
                    i += 1
                    continue
                elif ch2 == '-' or ch2 == ')' or ch2 == '(':
                    j += 1
                    continue
                else:
                    if int(ch1) == int(ch2):
                        i += 1
                        j += 1
                        k += 1
                    else:
                        return False

            return True
        
    else:
        if j-1 == len(n2):
            # _ code nomer
            #        nomer
            k = 0
            j = 1
            while k < 3:
                ch1 = n1[-i]
                ch2 = '495'[-j]

                if ch1 == '-' or ch1 == ')' or ch1 == '(':
                    i += 1
                    continue
                elif ch2 == '-' or ch2 == ')' or ch2 == '(':
                    j += 1
                    continue
                else:
                    if int(ch1) == int(ch2):
                        i += 1
                        j += 1
                        k += 1
                    else:
                        return False
                    
            return True
        
        else:
            # _ code nomer
            # _ code nomer
            k = 0
            while k < 3:
                ch1 = n1[-i]
                ch2 = n2[-j]

                if ch1 == '-' or ch1 == ')' or ch1 == '(':
                    i += 1
                    continue
                elif ch2 == '-' or ch2 == ')' or ch2 == '(':
                    j += 1
                    continue
                else:
                    if int(ch1) == int(ch2):
                        i += 1
                        j += 1
                        k += 1
                    else:
                        return False
            return True

NewNumber = input()
Old1 = input()
Old2 = input()
Old3 = input()

if Comparator(NewNumber,Old1):
    print("YES")
else:
    print("NO")
    
if Comparator(NewNumber,Old2):
    print("YES")
else:
    print("NO")

if Comparator(NewNumber,Old3):
    print("YES")
else:
    print("NO")
                
        
    
        
        
       
            

