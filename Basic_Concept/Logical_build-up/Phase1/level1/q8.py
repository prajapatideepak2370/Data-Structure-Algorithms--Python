#Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

temp = int(input("Enter the Temperature: "))

if temp <= 15:
    print("ITS COLD TODAY")
elif temp <= 30:
    print("ITS WARM TODAY")
else:
    print("ITS HOT TODAY")