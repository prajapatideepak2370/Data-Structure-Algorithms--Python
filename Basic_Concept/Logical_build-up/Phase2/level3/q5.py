# Print first n terms of a geometric progression (a, r). 
n = int(input("Enter the number: "))
gp = 0
a , r = 2, 3
for i in range(1, n+1):
    gp = a * r**(i - 1)
    print(gp)
