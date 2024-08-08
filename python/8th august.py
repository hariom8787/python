square=[]
for i in range(1,21):
    y=i*i
    square.append(y)
print(square)
#dictionaries
'''unorderd collection of arbitrary objects:
variable length,heterogeneous and arbitarirly nestable
table of objects refrences(hash table) '''
d={'name':'raghav','age':22,'roll_number':'A123'}
food={'dishes':{'maggie':3,'coke':7,'frenchfries':8}}#nested dictionary
for i in d.keys():
    print(i)
for i in d.values():
    print(i) 
for i,j in d.items():
    print(i,j) 
#change values in dictionary
d['name']='rajeev'
print(d)
#delete key
del d['name']
print(d) 
#len of dictionary
print(len(d) )    
def subsets(s):
    if not s :
        return [[]]
    subset=[]
    first=list(s)[0]
    rest=s-{first}
    for sub in subsets(rest):
        subset.append(sub)
        subset.append(subset+[first])
    return subset
s={1,2,3} 
for subs in subsets(s):
    print(subs)  
t=()
t=('name',)
t=(1,2,3,(3,5,6,))
t=tuple('name')
print(t)
dimension=(456,234)
number=(23,56,1,0,6,7,45,67,89)   
print(number.index(56))
print(number.count(0)) 