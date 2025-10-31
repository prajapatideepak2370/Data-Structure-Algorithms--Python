# Take a 3-digit number and check if the sum of the first and last digit equals the middle digit. 

num = int(input("Enter the 3-Digit number: "))
first = num // 100
last = num % 10
middle = num % 10 + num // 100

if (first + last) == middle:
    print("The sum of the first and last digit equals the middle digit.")
else:
    print("The sum of the first and last digit is not equals the middle digit.")