# Check whether a given integer is single-digit, double-digit, or multi-digit.

num = int(input("Enter the number: "))

# Handle negative numbers
num = abs(num)

if num < 10:
    print("Single-digit")
elif num < 100:
    print("Double-digit")
else:
    print("Multi-digit")
