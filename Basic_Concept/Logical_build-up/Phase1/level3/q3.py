# Take three numbers and print the median value (neither maximum nor minimum).
num1 = int(input("Enter the number1: ")) 
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
    median = num1
elif (num2 > num1 and num2 < num3) or (num2 > num3 and num2 < num1):
    median = num2
elif (num3 > num1 and num3 < num2) or (num3 > num2 and num3 < num1):
    median = num3
else:
    print("invlid")

print("The median value is:", median)