import math
x = int(input("Enter the number: "))
   
def is_armstrong(x):
    num = x
    total = 0   
    nod = len(str(x))  
    while num > 0:
            digit = num % 10
            total = total + (digit**nod)
            num = num // 10
    return total 

print(is_armstrong(x)== x)

'''
Dry Run: 
        Input: 153
        num = 153
        total = 0
        nod = 3

Iteration:
digit = 3, total = 27, num = 15
digit = 5, total = 152, num = 1
digit = 1, total = 153, num = 0
Total = 27+125+1 = 153
Output: True
            Time Complexity: O(log10(n))
            Space Complexity: O(1)
'''

# for i in range(1, int(math.sqrt(x)) + 1):
#     if x % i == 0:
#         print(i)
#         if i != x // i:
#             print(x // i)
