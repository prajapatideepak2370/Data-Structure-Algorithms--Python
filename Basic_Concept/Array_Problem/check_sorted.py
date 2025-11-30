nums = [5,6,7,8,9,10,1,11]
def sort_check(nums):
    n = len(nums)
    for i in range(0, n-1):
        if nums[i] > nums[i+1]:
            return False
    return True
print(sort_check(nums))