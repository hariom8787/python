#positional arguments
def pet(pet_name,pet_breed):
    print(f'my pet name is {pet_name}, and its breed is {pet_breed}')
pet('kalu','dog')
pet('dog','kalu')  
#key words arguments
def pet(pet_name,pet_breed):
    print(f'my pet name is {pet_name}, and its breed is {pet_breed}')
pet(pet_name='kalu',pet_breed='dog')
pet(pet_breed='cat',pet_name='shiny')
#optional parameters
def full_name(first_name,last_name,middle_name=''):
    if middle_name:
        print(f'{first_name} {middle_name} {last_name}')
    else:
        print(f'{first_name} {last_name}')
full_name('som','maurya','kumar')
full_name('som','maurya') 
#defualt parameters
def name(first_name,last_name='singh') :
    print(f'{first_name} {last_name}')   
name('sagar','kumar')
name('vishal')
# for arbitrary  positinal arguments
def pizza(size,*toppings):
    print(f'{size} and {toppings}')
pizza('32','capcicum')
pizza('16','capcimum','corn','extra cheese')
#  for arbitrary keyword arguments
def pizaa(*size,**toppings):
    y =toppings
    for value in y.values():
        print(value)
        
    print(f'sizes are {size} and toppings included {toppings}')
pizaa('16','32','32',toppings=('cheese','extra corn'))

  

      
    