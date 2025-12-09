nums = [2,0,2,1,1,0]
def BetterAppraoch(nums):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            cnt0 += 1
        elif nums[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    for i in range(0, cnt0):
        nums[i] = 0
    for j in range(cnt0, cnt0 + cnt1):
        nums[j] = 1
    for k in range(cnt0 + cnt1, len(nums)):
        nums[k] = 2
    return nums
# Time Complexity = O(2N) 
# Space Complexity = O(1)


def OptimalAppraoch(nums):  # Dutch National Flag algorithm.
    # Initialize three pointers: low and mid at 0, high at end
    low, mid, high = 0, 0, len(nums) - 1

    # Traverse until mid crosses high
    while mid <= high:
        # If element is 0, swap with low, move both low and mid forward
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        # If element is 1, just move mid forward
        elif nums[mid] == 1:
            mid += 1
        # If element is 2, swap with high, move only high backward
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums
# Time Complexity = O(N) 
# Space Complexity = O(1)
print(OptimalAppraoch(nums))
