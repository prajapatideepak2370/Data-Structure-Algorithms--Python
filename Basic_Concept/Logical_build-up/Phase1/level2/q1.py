#Take a 3-digit number and check if all digits are distinct. 

def distinct(num):
    st = str(num)

    return len(set(st)) == len(st)
num = int(input("Enter the Number: "))

if distinct(num):
    print("all digits are distinct")
else:
    print("all digits are not distinct")