# Print the sum of first n natural numbers.
n = int(input("Enter the number: "))
sumN = 0
for i in range(1, n, +1):
    sumN += i 
print("The sum of first N natural no.: ", sumN)



# Print the sum of all even numbers up to n.
sumE = 0
for i in range(1, n , +1):
    if i % 2 == 0:
        sumE += i
print("The sum of all even numbers: ", sumE)



#Print the sum of all odd numbers up to n. 
sumO = 0 
for i in range(1, n , +1):
    if i % 2 != 0:
        sumO += i
print("The sum of all odd numbers: ", sumO)
