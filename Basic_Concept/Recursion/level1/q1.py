# Print numbers from 1 to n using recursion.

def fun(n):
    if  n > 0:
        fun(n -1)
        print(n)

print(fun(5))

# Print numbers from n down to 1 using recursion. 
def func(y):
    if y > 0:
        print(y)
        func(y - 1)
print(func(5))
    