from typing import Any


# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sit(self):
#         print(f'{self.name} is now sitting') 
#     def roll_over(self):
#         print(f'{self.name} rolled over')
# my_dog=Dog('labru',7)
# print(f"my dog's name is {my_dog.name}")
# print(f"my dog's age is {my_dog.age} years old")        
# my_dog.sit()
# my_dog.roll_over()
# #inheritance



# class Car:
#     def __init__(self,make,model,year=''):
#         self.make=make
#         self.model=model
#         self.year=year
#     def get_des_name(self):
#         l_name=f'{self.year} {self.make} {self.model}'
#         return l_name.title()
# my_car=Car('audi','a8','2016') 
# print(my_car.get_des_name())  
# class Elec_car(Car):
#     def __init__(self,make,model):
#         super().__init__(make,model)
# my_c=Elec_car('maruti','800')   
# print(my_c.get_des_name())
     


      
class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return (self.a)/(self.b)
    
my_calc=Calc(2555,5339)
print(my_calc.div())

my_calc1=Calc(23,23)
print(my_calc1.mul())