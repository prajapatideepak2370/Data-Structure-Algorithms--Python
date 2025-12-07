nums = [2,2,1]

def bruteApproach(nums): # Linear Search
    n = len(nums)
    for i in range(0, n):
        num = nums[i]
        cnt = 0
        for j in range(0, n):
            if nums[j] == num:
                cnt += 1
        if cnt == 1:
            return num
# Time Complexity = O(N1 * N2) ----> O(N^2)
# Space Complexity = O(1)

def BetterApproach(nums):
    n = len(nums)
    maxi = max(nums)
    freq = [0] * (maxi + 1)
    for num in nums:
        freq[num] += 1

    for num in nums:
        if freq[num] == 1:
            return num
    
    return None  # if no non-repeating element
# Time Complexity = O(N1 + N2 + N3) ----> O(3N)
# Space Complexity = O(N)

def optimalApproach(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor
# Time Complexity = O(N) 
# Space Complexity = O(1)