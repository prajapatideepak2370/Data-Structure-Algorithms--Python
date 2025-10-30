# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin. 

x = int(input("Enter the X-axis coordinate: "))
y = int(input("Enter the Y-axis coordinate: "))

if (x == 0) and (y == 0):
    print("Coordinate at the Origin")
elif (y == 0 ) and (x != 0):
    print("Coordinate at the X-axis")
else:
    print("Coordinate at the Y-axis")