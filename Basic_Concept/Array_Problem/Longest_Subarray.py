nums = [1,2,3,1,1,1,1,5,7,3,2,1]
k = 3
def BruteForce(nums, k):
    n = len(nums)
    maxlength = 0
    for startInx in range(n):
        for endInx in range(startInx, n):
            cntSum = 0
            for i in range(startInx, endInx + 1):
                cntSum += nums[i]
            if cntSum == k:
                maxlength = max(maxlength, endInx - startInx + 1)
    return maxlength
# Time Complexity = O(N^3) 
# Space Complexity = O(1)