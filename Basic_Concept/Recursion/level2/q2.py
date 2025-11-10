# Reverse a number recursively.

def reverse(n, rev = 0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev*10 + digit
    return reverse(n // 10, rev)

print(reverse(3432))


