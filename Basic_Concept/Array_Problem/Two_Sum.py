nums = [2,7,11,15]
target = 9
def two_sum(nums, target):
    
    for i in range(0, len(nums)-1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return i , j
            else:
                j+=1
        i +=1

print(two_sum(nums, target))                   