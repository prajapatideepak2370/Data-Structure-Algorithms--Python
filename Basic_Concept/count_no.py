n= int(input("Enter the 1st number:"))
x = int(input("Enter the 2nd number:"))
#Create a function to count the number of digits in a number
def count_num(n):
    count = 0           #Make a count variable to store the number of digits 
    while n >0:         #Run a loop until n becomes 0
        n = n//10       #Remove the last digit from n
        count +=1       #last digit removed, increase the count by 1
    return count

count = count_num(n) #Function call
print("The number of digits in the number is:",count)


'''
Dry Run:
       n = 4567 -->  n//10 --> 4567/10 :- 7 --> count=1
       n = 456 -->  n//10 --> 456/10 :- 6 --> count=2
       n = 45 -->  n//10 --> 45/10 :- 5 --> count=3
       n = 4 -->  n//10 --> 4/10 :- 0.4 (using flow division then it means 0) --> count=4
       n = 0 --> loop ends here
Time complexity: O(n)             ---where n is the number of digits in the number
Space complexity: O(1)
'''

#------------------------------------------2nd Method Using LOGs-------------------------------------------------#
from math import*

def log_count(x):
    return int(log10(x)+1)
cout = log_count(x)
print("The number of digits in the number is:",cout)

'''
Dry run: 
         x = 4567
         log10(4567) = 3.659
         3.659 + 1 = 4.659
         int(4.659) = 4
Time complexity: O(log10(n))       -----where n is the number of digits in the number
Space complexity: O(1)

'''