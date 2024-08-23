'''a=12
def add():
     a=15
     print(a)
     def one():
         global a
         a=17
         print(a)
     one()
add() 
print (a) 
var =99
def local():
    var=0
def glob1():
    global var
    var+=1    
def glob2():
    var=0
    import scope
    scope.var+=1
def glob3():
    var=0
    import sys
    glob=sys.modules['scope']
    glob.var+=1
def test():
    print(var) 
    local()
    glob1();glob2();glob3()
    print(var)
test()
print(var) 
# lambda functions
# lambda = arguments:expression
list=['ram','raghav','annil','abhi']
soreted_names=sorted(list,key=lambda x: x.lower()) 
print(soreted_names)
num=[1,2,3,4,5]
print(num)
squared_numbers=list(map(lambda x:x**2,num))
print(squared_numbers)'''
import sys
a=9
print(sys.argv)
                     