# Print the factorial of a given number. 
n = int(input("Enter the number: "))
fac = 1
for i in range(1, n, +1):
    fac *= i
print("The Factorial of Number is: ", fac)


# Print the product of digits of a given number.

total = 1
while n > 0:
    digit = n % 10
    total = total*digit 
    n = n // 10
print("Product of digits: ",total)