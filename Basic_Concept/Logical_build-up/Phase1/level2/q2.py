#Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 

num = int(input("Enter the Number: "))
first = num // 100
second = (num //10) % 10
third = num % 10

if (second > first) and (second > third):
    print("Middle digit is the largest.")
elif(second < first) and (second < third):
    print("Middle digit is the smallest.")

else:
    print("Neither")
