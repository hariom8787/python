"""i=0
while(i<10):
    i=i+1
    print(i)"""
    

"""name=str(input("Enter a name\t"))
while(name!="q"):
    print(name)
    name=str(input("Enter a name\t"))"""


i=1
while(i<=10):
    #print("12*",i)
    print(f'12*{i}={12*i}')
    i=i+1
def add(a,b):
    #utfjvhvkh
    #'''function to add'''
    #print("vd")
   
    '''function to add'''
    print(add.__doc__)
    return(a+b)
print(add(3,5))
  
  
def add(x,y):
    c=x+y
    print(c)

def sub(x,y):
    c=abs(x-y)
    print(c)

def mul(x,y):
    c=x*y
    print(c)

def div(x,y):
    c=x/y
    print(c)

  
#x=int(input("enter the value of x"))  
#y=int (input("enter the value of y"))
#op=input("operation you want?")
s=input("--program started----\n please take a space between operands \& operator\n")
x,op,y=s.split()
x=int(x)
y=int(y)
if op=='+':
   add(x,y)
elif op=='-':
    sub(x,y)
elif op=='*':
    mul(x,y)
elif op=='/':
    div(x,y)
else:
    print(" check your values or operation(+,-,*,/)") 
   
