nums = [1,1,1]
k = 2
def bruteforce(nums, k):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for m in range(i, j+1):
                sum = sum + nums[m]
            if sum == k:
                cnt +=1
    return cnt
    # Time Complexity :- O(N*N*N) ~ O(N^3)
    # Space Complexity:- O(1)

def betterApproach(nums, k):
    cnt = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum = sum + nums[j]
            if sum == k:
                cnt +=1
    return cnt
    # Time Complexity :- O(N*N) ~ O(n²)
    # Space Complexity:- O(1)

def OptimalApproach(nums, k):
    prefixsumCnt= {}
    prefixSum= 0  
    cnt = 0
    prefixsumCnt[0] = 1
    for i in range(len(nums)):
        prefixSum += nums[i]
        remove = prefixSum - k
        if remove in prefixsumCnt:
            cnt += prefixsumCnt[remove]
        prefixsumCnt[prefixSum] = prefixsumCnt.get(prefixSum, 0) + 1
    return cnt
    # Time Complexity :- O(N) 
    # Space Complexity:- O(N) 
print(OptimalApproach(nums, k))