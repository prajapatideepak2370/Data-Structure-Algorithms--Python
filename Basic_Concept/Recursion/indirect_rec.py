
# Indirect Recursion:- When a function calls another function and that function calls the first function, it is called Indirect Recursion.
def func_a(count_a):
    if count_a == 0:
        return
    print("Function A is Called")
    func_b(count_a - 1)

def func_b(count_b):
    if count_b == 0:
        return
    print("Function B is Called ")

func_a(2)