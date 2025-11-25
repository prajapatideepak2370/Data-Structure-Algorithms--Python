# Check if a number is a palindrome using recursion.
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

def is_Palindrome(n):
    return n == reverse_number(n)


print(is_Palindrome(121))   # True
print(is_Palindrome(12321)) # True
print(is_Palindrome(1234))  # False
