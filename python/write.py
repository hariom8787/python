file=open('three.txt','w')
h='harsh mohan nigam'
file.write(h)
file.write('hi there\n')
file.write('python file handeling')
file=open('one.txt','w')
file.write('hi\n')
file.write('hello')
file.close()
#with statement in writing of file
with open('four.txt','w') as file:
    file.write('hello world!')
    