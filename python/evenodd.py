list=[4,2,3,7,5,8,9]
print(list)

l1=[]
l2=[]
for i in list:
    if i&1==0:
        l1.append(i)
    else:
        l2.append(i)  
print(l1)
print(l2)           