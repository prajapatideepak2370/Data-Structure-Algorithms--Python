# Make a Recursive Function to Reverse a Array 

def Reverse_Arr(arr, left, right):
    if left >= right:
        return 
    arr[left], arr[right] = arr[right], arr[left]
    Reverse_Arr(arr, left + 1, right - 1)
    return arr

arr = [4,6,3,6,9,8,0]
print("The Reversed Array is:", Reverse_Arr(arr, 0, len(arr) - 1))

'''
Dry Run:
arr = [4,6,3,6,9,8,0]
left = 0, right = 6
Reverse_Arr(arr, 0, 6)
arr[0], arr[6] = arr[6], arr[0] --> arr = [0,6,3,6,9,8,4]
Reverse_Arr(arr, 1, 5)
arr[1], arr[5] = arr[5], arr[1] --> arr = [0,8,3,6,9,6,4]
Reverse_Arr(arr, 2, 4)
arr[2], arr[4] = arr[4], arr[2] --> arr = [0,8,9,6,3,6,4]
Reverse_Arr(arr, 3, 3)
left >= right --> return

Time Complexity: O(n/2) = O(n)
Space Complexity: O(n/2) = O(n) --> due to the recursion stack space
'''