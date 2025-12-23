# Rearrange Array Elements by Sign
nums = [3,1,-2,-5,2,-4]
def BruteForce(nums):
    neg = []
    pos = []
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    result = []
    for i in range(min(len(pos), len(neg))):
        result.append(pos[i])
        result.append(neg[i])
    
    result.extend(pos[len(neg):])
    result.extend(neg[len(pos):])
    return result
# Time Complexity = O(N1 + N2) ----> O(2N)
# Space Complexity = O(N)
print(BruteForce(nums))

def Optimal(nums):
    ans = [0] * len(nums)
    posInd = 0
    negInd = 1
    for num in nums:
        if num < 0:
            ans[negInd] = num
            negInd += 2
        else:
            ans[posInd] = num
            posInd += 2
    return ans 
# Time Complexity = O(N) 
# Space Complexity = O(N)
print(Optimal(nums))