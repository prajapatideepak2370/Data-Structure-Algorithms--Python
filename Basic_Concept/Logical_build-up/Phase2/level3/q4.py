# Print first n terms of an arithmetic progression (a, d). 
n = int(input("Enter the number: "))
ap = 0
a , d = 3, 5
for i in range(1, n+1):
    ap = a + (i - 1)*d
    print(ap)
