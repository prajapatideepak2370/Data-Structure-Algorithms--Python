#Make a  Parametrized Recursive Function to Calculate the Sum of 1 to N 

# ---> OPTIMIZED CODE <---
def total_sum(n):
   if n == 1: 
      return 1
   return n + total_sum(n - 1) 

n = int(input("Enter the number N:"))
print("The total sum is:", total_sum(n))

'''
Time complexity: O(n)
Space complexity: O(n) --> due to the recursion stack space
'''