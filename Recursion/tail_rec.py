#Tail Recursion:- A function that makes a recursive call as its last operation is called Tail Recursion.
count_tail = 0
def tail_func():
    global count_tail
    if count_tail == 5:
        return
    count_tail +=1
    tail_func()
    print("Hello Python World!!!")
tail_func()


'''
Dry Run: 
count = 0
func() -> count = 0
      count != 5
        count = 1
        call func() -> count = 1
            count != 5
            count = 2
            call func() -> count = 2
                count != 5
                count = 3
                call func() -> count = 3
                    count != 5
                    count = 4
                    call func() -> count = 4
                        count != 5
                        count = 5
                        call func() -> count = 5
                            if count == 5: 
                                return
                        func() return   Recursion End here 
                    print("Hello Python World!!!") -> Hello Python World!!!
                    func() return
                print("Hello Python World!!!") -> Hello Python World!!!
                func() return
            print("Hello Python World!!!") -> Hello Python World!!!
            func() return
        print("Hello Python World!!!") -> Hello Python World!!!
        func() return
    print("Hello Python World!!!") -> Hello Python World!!!
    func() return 

End here the Recursion code   
Time complexity: O(n+1) = O(n)            
Space complexity: O(n+1) = O(n)  
'''