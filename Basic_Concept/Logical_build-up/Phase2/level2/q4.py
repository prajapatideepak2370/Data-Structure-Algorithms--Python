# Find the sum of digits of a number.

n = int(input("Enter the number: "))
sum = 0
num = n
while num>0:
    digit = num % 10 
    sum = sum + digit
    num = num // 10
print("The sum of digit of a number: ",sum)