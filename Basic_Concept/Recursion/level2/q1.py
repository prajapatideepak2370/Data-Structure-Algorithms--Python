# Count the number of digits in a number recursively. 
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

n = int(input("Enter the number: "))
print(count_digits(n))