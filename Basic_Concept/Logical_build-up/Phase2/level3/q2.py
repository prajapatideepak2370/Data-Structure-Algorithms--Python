# Find HCF (GCD) of two numbers using loops

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

sm = min(n1, n2)  
hcf = 1            

for i in range(1, sm + 1):
    if (n1 % i == 0 and n2 % i == 0):
        hcf = i    # update HCF whenever a common factor is found

print("HCF: ", hcf)
