# Make a Recursive Function to check if a String is Palindrome or not

def is_Palindrome(s, left, right):
    if left >= right:
        return True

    s[left], s[right] = s[right], s[left]
    is_Palindrome(s, left +1, right -1)
    return s

s = str(input("Enter the String:"))
print("The String is Palindrome:", is_Palindrome(list(s), 0, len(s) -1) == list(s))

'''
Time Complexity: O(n/2) = O(n)
Space Complexity: O(n/2) = O(n) --> due to the recursion stack space
'''