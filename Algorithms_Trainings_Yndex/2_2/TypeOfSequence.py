
a = 0

constant = 0 # if thet every number will be equale to the previouse
ascending = 0 # if thet every number will be greater then previous
weak_ascending = 0 # if thet every number will be no less then previouse (exists number thet is equale to the previouse)
descending = 0 # if thet every number will be less then the previouse
weak_descending = 0 # if thet every number will be no greater then the priviouse

prev = 0
i = 0
can_be_weak_as = False
can_be_weak_des = False

while a != -2*10**9:
    a = int(input())
    if i != 0:
        d = a - prev
        if a != -2*10**9:
            if d == 0:
                constant += 1
                weak_ascending += 1
                weak_descending += 1
            elif d < 0:
                descending += 1
                weak_descending += 1
            else:
                ascending += 1
                weak_ascending += 1
                
                
                    
    prev = a
    i += 1

if constant == i-2:
    print("CONSTANT")
elif ascending == i-2:
    print("ASCENDING")
elif weak_ascending == i-2:
    print("WEAKLY ASCENDING")
elif descending == i-2:
    print("DESCENDING")
elif weak_descending == i-2:
    print("WEAKLY DESCENDING")
else:
    print("RANDOM")







    
    
