
# Indirect Recursion:- When a function calls another function and that function calls the first function, it is called Indirect Recursion.
def func_a(count_a):
    if count_a == 0:
        return
    print("Function A is called")
    # func_b(count_a - 1)