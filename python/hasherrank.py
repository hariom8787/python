n=int(input("Enter the value of n"))
if n % 2 != 0:
    print("Weird")
else:
    if 2<n<5:
        print("Not Weird")
    elif 6<n<20:
        print("Weird")
    elif 20<n:
        print("Not Weird")
