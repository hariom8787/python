file=open('one.txt','r')
for line in file:
    print(line)
file=open('one.txt','r')
print(file.read())  
with open('one.txt','r') as file:
    d=file.read()
print(d) 
with open('two.txt','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)
f=open('two.txt','r')
print(f.readlines(2))
        