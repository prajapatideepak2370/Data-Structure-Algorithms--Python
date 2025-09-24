'''
10 = [1,2,5,10]
'''
n = int(input("Enter the number: "))
#Brute Force Approach
def prime_Factor(n):
    factors = []
    for i in range(1, n+1): 
        if n % i == 0:
            factors.append(i)
    return factors

'''
Dry Run: 
        Input: 10
        factors = []
        i = 1, 10%1=0 factors = [1]
        i = 2, 10%2=0 factors = [1,2]
        i = 3, 10%3=0 factors = [1,2]
        i = 4, 10%4=0 factors = [1,2]
        i = 5, 10%5=0 factors = [1,2,5]
        i = 6, 10%6=4 factors = [1,2,5]
        i = 7, 10%7=3 factors = [1,2,5]
        i = 8, 10%8=2 factors = [1,2,5]
        i = 9, 10%9=1 factors = [1,2,5]
        i = 10,10%10=0 factors = [1,2,5,10]
Output: [1,2,5,10]
            Time Complexity: O(n)
            Space Complexity: O(1)  

'''
# Optimized Approach
import math
def prime_Factor_Optimized(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1): #1 to √n +1 means like n is 10 then √10=3.16 so 1 to 4 
        if n % i == 0:
            factors.append(i)
            if i != n // i: # to avoid duplicate factors when n is a perfect square like 36 = 1,2,3,4,6,9,12,18,36 here 6*6=36 so we want to add 6 only once
                factors.append(n // i)
    factors.sort()
    return factors
print(prime_Factor_Optimized(n))
'''
Dry Run:
        Input: 10
        factors = []
        in for loop i=1 to int(√10 ->(3.16)) +1 = 3+1 =4
        i = 1, 10%1=0 factors = [1,10]
        i = 2, 10%2=0 factors = [1,10,2,5]
        i = 3, 10%3=1 factors = [1,10,2,5]
Output: [1,2,5,10]
            Time Complexity: O(√n) + O(nlogn)
            Space Complexity: O(1)
'''