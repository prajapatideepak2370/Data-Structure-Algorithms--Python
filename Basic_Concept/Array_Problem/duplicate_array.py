nums = [1,1,1,2,2,3,3,3,3,4,4,5,5,5,5,6,6,7,7,8,9,9,9,10,10]

def duplicateArr(nums):  # BRUTE FORCE APPROACH
    n = len(nums)
    freq_map = {}
    for i in range(0, n):
        freq_map[nums[i]] = 0
    j = 0
    for k in freq_map:
        nums[j] = k
        j += 1
    return j
    # TC = O(2N) ~ O(N)
    # SC = O(N)

print(duplicateArr(nums))