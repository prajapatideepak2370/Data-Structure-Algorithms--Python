# Calculate power of a number (xⁿ) using recursion.

def pow(y, n):
    if n == 0:
        return 1
    return y * pow(y, n-1)
print(pow(2, 5))
    