n = int(input("Enter a number: "))

def is_palindrome(n): #Function to check if a number is palindrome or not
    reverse = 0 #Create a variable to store the reverse of the number
    result = n #Store the original number in another variable
    while n>0:#Run a loop until n becomes 0
        digit = n%10 #Get the last digit of n
        reverse = reverse*10+digit #Append the last digit to the reverse variable
        n = n//10 #Remove the last digit from n 
    return result == reverse #Check if the original number is equal to the reverse number

print(is_palindrome(n))

'''
Dry Run:
1st---> n = 121                               
        result = 121
        reverse = 0
        digit = 121%10 = 1
        reverse = 0*10 + 1 = 1 

2nd---> n = 121//10 = 12
        digit = 12%10 = 2
        reverse = 1*10 + 2 = 12

3rd---> n = 12//10 = 1
        digit = 1%10 = 1
        reverse = 12*10 + 1 = 121

4rd---> n = 1//10 = 0
        loop ends here
        return 121 == 121 --> True
Time complexity: O(log10(n))          
Space complexity: O(1)
'''
