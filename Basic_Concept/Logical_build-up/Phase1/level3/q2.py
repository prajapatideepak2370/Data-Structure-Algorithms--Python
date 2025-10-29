# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and “FizzBuzz” if divisible by both. 

num = int(input("Enter the number: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif (num % 3 == 0):
    print("Fizz")
else:
    print("Invild")