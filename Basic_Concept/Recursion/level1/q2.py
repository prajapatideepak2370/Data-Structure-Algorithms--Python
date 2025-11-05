# Print only even numbers from 1 to n recursively.

def func_A(n):
    if n > 0:
        func_A(n - 1)
        if n % 2 == 0:
            print(n)
print(func_A(10))
  
# Print only odd numbers from 1 to n recursively. 

def func_B(y):
    if  y > 0:
        func_B(y - 1)
        if y % 2 != 0:
            print(y)
print(func_B(10))

# Print sum of first n natural numbers recursively. 

def sum_N(a):
    sum = 0
    if a > 0:
        func_A(a - 1)
        sum += a
    return sum
print(sum_N(10))
    