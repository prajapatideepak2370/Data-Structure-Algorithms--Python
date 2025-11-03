# Find LCM of two numbers using loops.

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

lg = max(n1, n2)
lcm = 1
while True:
    if(lg % n1 == 0 and lg % n2 == 0):
        lcm = lg   # update LCM whenever a common factor is found
        break      # break the loop because found the smallest such number
    lg +=1
print("LCM: ", lcm)