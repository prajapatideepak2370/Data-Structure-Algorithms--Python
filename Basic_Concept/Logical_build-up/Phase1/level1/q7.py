# Take three numbers and print the largest
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
num3 = int(input("enter the num3: "))

if (num1 > num2) and (num1 > num3):
    print("NUM1 IS LARGEST ONE")
elif (num2 > num1) and (num2> num3):
    print("NUM2 IS LARGEST ONE")
elif (num3 > num1) and (num3 > num2):
    print("NUM2 IS LARGEST ONE")
else:
    print("All numbers are equal or two are equal")
