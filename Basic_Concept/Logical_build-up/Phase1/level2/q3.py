# Take a 4-digit number and check if the first and last digits are equal. 

num = input("Enter the 4 digit number: ")

if len(num) == 4 and num.isdigit():
    if num[0] == num[-1]:
        print("The first and last number digits are equal")
    else:
        print("The first and last number digits are not equal")
else:
    print("Please enter a valid 4-digit number.")
    

