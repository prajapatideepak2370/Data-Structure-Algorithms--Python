# Check if a number is a perfect number. 

n = int(input("Enter the number: "))
div = []
for i in range(1, n):
    if n % i == 0:
        if n != i:
            div.append(i)
print("The number divisors are: ", div)

div_sum = 0
for i in range(0 , len(div)):
    div_sum += div[i]
print("The number divisors sum are: ", div_sum)

if n == div_sum:
    print("A number is a Perfect number")
else:
    print("A number is not a Perfect number")


