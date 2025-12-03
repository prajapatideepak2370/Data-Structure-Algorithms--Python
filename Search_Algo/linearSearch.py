nums = [3,4,5,6,7,8,9]
target = int(input("Enter the Target: "))
def linear_search(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i
    return -1
print(linear_search(nums, target))

# Time Complexity= O(n)
# Space Complexity = 0(1)
