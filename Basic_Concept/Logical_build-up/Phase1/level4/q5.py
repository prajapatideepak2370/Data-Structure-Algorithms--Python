# Take three numbers and check if they are in geometric progression. 

x = int(input("Enter the number1: "))
y = int(input("Enter the number2: "))
z = int(input("Enter the number3: "))

if (y**2) == (x * z):
    print("They are in Geometric Progression")
else:
    print("They are not in Geometic Progression")