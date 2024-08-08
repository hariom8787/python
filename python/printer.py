list=['java','html','python','javascript','php','cotlin','css']
print(list)
l1=[]
l2=[]
for i in list:
    if len(i)>=4:
        print(f'I know {i}.this is good language')
        l1.append(i)
    else:
        print(f'I dont know{i}.I have to learn this')
        l2.append(i)