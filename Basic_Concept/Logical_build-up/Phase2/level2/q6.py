# Print Fibonacci series up to n terms. 
# print 0,1,1,2,5,8,13,...etc

n = int(input("Enter the Number: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b  # Update the values of a and b
    count += 1



