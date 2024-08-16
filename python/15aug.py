
 
 
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
l=[1,7,26,11,31,33,36,47,42,49,50]
for i in l:
    r=int(i**.5)
    if r**2==i:
        l.remove(i)
print(l)
for i in l:
    r=int(i**.5)
    if r**2==i:
        pass
    print(i)
print(1**0.5)
print(10**0.5)
cars=['bmw','alto','i20','jaguar']
agency_order=['breza','ritara','fortune','alto']
for i in agency_order: 
    if i in cars:
        print(f'{i} - already')
    else:
        print(f'{i} - not available')