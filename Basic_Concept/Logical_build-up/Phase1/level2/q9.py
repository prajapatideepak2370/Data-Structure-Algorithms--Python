# Check whether a number is a perfect square (without using the square root function).

num= int(input("Enter the Number: "))

n = num
odd = 1  # first odd number

while n > 0:
    n -= odd     # subtract current odd number
    odd += 2      # move to next odd number

if n == 0:
    print(num, "is a perfect square.")
else:
    print(num, "is NOT a perfect square.")
