# Print the reverse of a given number. 

n = int(input("Enter the Number: "))
num = n
rev = 0 
nod = len(str(n))
while num > 0:
    digit = num % 10
    rev = rev *10+digit
    num = num // 10
print("The reverse number is: ",rev)