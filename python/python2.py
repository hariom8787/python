name=[]
name=['sam','abhi','raj','aman']
print(name[2])
print(name[-1])
print(f'my name is {name[2]}')
#modifying element
name[0]='ram'
print(name)
#adding element in a list
#appen method
name.append('abhishek')
print(name)
#insert method
name.insert(0,'anuj')
print(name)
even=[]
odd=[]
for i in name:
    if len(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)   
#remove element from list
#del statement
del name[0]
print(name) 
#remove method
name.remove('raj')  
print(name)   
del_name=name.pop()
print(name)
print(del_name)
Name=[]
for i in name:
    x= f'{i.title()}'
    Name.append(x) 
print(name) 
print(Name)  
mixed=['aman','raj',1,2,7,'abhi','samar',9,10,'rajeev'] 
ns=[]
num=[]
for i in mixed:
    if type(i)==str:
        x=f'{i.title()}'
        ns.append(x)
    else:
        num.append(i) 
print(mixed)
print(ns)
print(num) 
#ns.sort()
#print(ns) 
#ns.sort(reverse=True) 
#print(ns)
x=sorted(ns)
print(x)
print(ns)
ns.sort()
print(ns)
name.reverse()
print(name)



  
        
