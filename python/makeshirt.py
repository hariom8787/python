'''def make_shirt(size,msg):
    print(f'size of shirt is {size} and the text of msg is {msg}')
make_shirt('32','coding is life')
make_shirt(msg='Coding is life',size='32')'''

def modified_make_shirt(size,msg=" i love python"):
    if size=='l':
        print(f'size of shirt is {size} and the text of msg is {msg}')
    elif size=='m':
        print(f'size of shirt is {size} and the text of msg is {msg}')
    else:
        print(f'size of shirt is {size} and the text of msg is --i prefer any size except l & m ')
    #print(f'size of shirt is {size} and the text of msg is {msg}')
modified_make_shirt('l','coding is life')
modified_make_shirt(msg='Coding is life',size='32')