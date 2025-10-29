# Take coordinates (x, y) and determine which quadrant the point lies in. 

x = int(input("Enter the Number X: "))
y = int(input("Enter the Number Y: "))

if (x > 0) and (y > 0):
    print("Quadrant of the point lies 1")
elif (x < 0 ) and (y > 0):
    print("Quadrant of the point lies 2")
elif (x < 0 ) and (y < 0):
    print("Quadrant of the point lies 3")
elif (x > 0 ) and (y < 0):
    print("Quadrant of the point lies 4")
else:
    print("INVLID COORDINATES")