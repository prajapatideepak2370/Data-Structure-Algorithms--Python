# Take three numbers and check if they are in arithmetic progression. 

x = int(input("Enter the number1: "))
y = int(input("Enter the number2: "))
z = int(input("Enter the number3: "))

if (2*y) == (x + z):
    print("They are in Arithmetic Progression")
else:
    print("They are not in Arithmetic Progression")