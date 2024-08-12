my_list=[]
for i in range(1,8):
    for j in range(i):
        my_list.append(i)
print(my_list) 
new_list=[]
for i in my_list:
    if i not in new_list:
        new_list.append(i)  
print(new_list) 
variable=set(my_list)
new_list=list(variable)
print(new_list) 
#set methods
my_set={1,2,3,4}
my_set.add(45)
my_set.remove(1)
my_set.discard(23)
my_set.pop(3)
my_set.clear()
#frozen sets
''' frozensets are immutable sets,meaning they caant be modified after creation'''
my_frozenset=frozenset([1,2,3,4,5]) 
print(my_frozenset) 
 
