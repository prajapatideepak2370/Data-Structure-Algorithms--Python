#Tree Recursion:- A function that makes more than one recursive call is called Tree Recursion.
def tree_func(count_tree):
    if count_tree == 0:
        return
    print("Hello Python World!!!")
    tree_func(count_tree - 1)
    tree_func(count_tree - 1)
tree_func(3) # you can change the value to see the output

'''
Dry Run:
count = 3
func(3) -> count = 3
    count != 0
    print("Hello Python World!!!") -> Hello Python World!!!
    func(2) -> count = 2
        count != 0
        print("Hello Python World!!!") -> Hello Python World!!!
        func(1) -> count = 1
            count != 0
            print("Hello Python World!!!") -> Hello Python World!!!
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
        func(1) return
        func(1) -> count = 1
            count != 0
            print("Hello Python World!!!") -> Hello Python World!!!
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
        func(1) return
    func(2) return
    func(2) -> count = 2
        count != 0
        print("Hello Python World!!!") -> Hello Python World!!!
        func(1) -> count = 1
            count != 0
            print("Hello Python World!!!") -> Hello Python World!!!
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
        func(1) return
        func(1) -> count = 1
            count != 0
            print("Hello Python World!!!") -> Hello Python World!!!
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
            func(0) -> count = 0
                if count == 0: 
                    return
            func(0) return
        func(1) return
    func(2) return
func(3) return
Time complexity: O(n+1) = O(n)            
Space complexity: O(n+1) = O(n)  
'''