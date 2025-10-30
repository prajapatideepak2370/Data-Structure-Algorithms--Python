# Take three numbers and check if they can form a Pythagorean triplet.

x = int(input("Enter the number1: "))
y = int(input("Enter the number2: "))
z = int(input("Enter the number3: "))

if max(x,y,z):
    if ((x**2) + (y**2) == (z**2)) :
        print(f"({x}, {y}, {z}) form a Pythagorean triplet")
    else:
        print(f"({x}, {y}, {z}) do NOT form a Pythagorean triplet.")
else:
    print("Invlid")
