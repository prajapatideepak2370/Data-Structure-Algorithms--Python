# Make a Recursive Function to calculate the factorial  of a Number 

def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter the number N:"))
print("The factorial is:", factorial(n))

'''
Dry Run:
n = 5
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
factorial(5) = 5 * 24 = 120


Time Complexity: O(n)
Space Complexity: O(n) --> due to the recursion stack space
'''