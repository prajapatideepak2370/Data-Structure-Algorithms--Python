# Check if a number is a palindrome.

n = int(input("Enter the Number: "))
num = n
rev = 0
nod = len(str(n))
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10
print(rev)
if n == rev:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")