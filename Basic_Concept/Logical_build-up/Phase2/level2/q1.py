# Count the number of digits in a given number. 
n = int(input("Enter the Number: "))
count = 0
while n > 0:
    total = n % 10
    count +=1
    n = n // 10
print("The number of digit is: ",count)