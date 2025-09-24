arr = [2,3,4,5,6]
def sum_rec(arr):
    if not arr: #Make a condition that if array is empty then recursion should stop
        return 0
    return arr[0] + sum_rec(arr[1:]) # Add the first element of the array to the sum of the rest of the array 
print(sum_rec(arr))  # Output: 20

'''
Dry Run:
arr = [2,3,4,5,6]
func([2,3,4,5,6]) -> arr is not empty
    return [2] + func([3,4,5,6]) -> arr is not empty
        return [3] + func([4,5,6]) -> arr is not empty
            return [4] + func([5,6]) -> arr is not empty
                return [5] + func([6]) -> arr is not empty
                    return [6] + func([]) -> arr is empty
                        return 0
                    return 6 + 0 = 6
                return 5 + 6 = 11
            return 4 + 11 = 15
        return 3 + 15 = 18
    return 2 + 18 = 20

'''