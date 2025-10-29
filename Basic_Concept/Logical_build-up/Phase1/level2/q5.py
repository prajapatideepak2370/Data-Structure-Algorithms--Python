# Check if a number is a multiple of 7 or ends with 7. 

nums = int(input("Enter the Number: "))
last  = nums % 10
if nums % 7 == 0 and last == 7:
    print("A number is a multiple of 7 or ends with 7")
else:
    print("A number is not a multiple of 7 or not ends with 7")