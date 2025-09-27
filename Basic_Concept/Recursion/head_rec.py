#Head Recursion:- A function that makes a recursive call as its first operation is called Head Recursion. 

count_head =0
def head_func():
    global count_head # to modify the global variable
    if count_head == 5: #Make a Condition to stop the Recursion and this is called Base Condition
        return
    print("Hello Python World!!!") 
    count_head +=1
    head_func()
head_func()

'''
Dry Run:

count = 0
func() -> count = 0
    count != 5
    print("Hello Python World!!!") -> Hello Python World!!!
    count = 1
    func() -> count = 1
        count != 5
        print("Hello Python World!!!") -> Hello Python World!!!
        count = 2
        func() -> count = 2
            count != 5
            print("Hello Python World!!!") -> Hello Python World!!!
            count = 3
            func() -> count = 3
                count != 5
                print("Hello Python World!!!") -> Hello Python World!!!
                count = 4
                func() -> count = 4
                    count != 5
                    print("Hello Python World!!!") -> Hello Python World!!!
                    count = 5
                    func() -> count = 5
                        if count == 5: 
                            return
                    func() return   Recursion End here 
Time complexity: O(n+1) = O(n)            
Space complexity: O(n+1) = O(n)
'''