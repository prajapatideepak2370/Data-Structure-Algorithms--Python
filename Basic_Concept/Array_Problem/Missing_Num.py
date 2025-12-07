arr = [1,2,4,5,6]
n = len(arr)
def miss_BruteApproach(arr , n):
    for i in range(1, n):
        flag = 0
        for j in range(0 , n-1):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
# Time Complexity = O(N1 * N2) ----> O(N^2)
# Space Complexity = O(1)

def miss_OptimalApproach(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
# Time Complexity = O(N) 
# Space Complexity = O(1)