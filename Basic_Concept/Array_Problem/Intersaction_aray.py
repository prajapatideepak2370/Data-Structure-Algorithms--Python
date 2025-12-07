arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,7]

def intersaction_BruteForce(arr1, arr2):   # Brute Force Approach 
    n1 = len(arr1)
    n2 = len(arr2)
    vis = [0] * len(arr2)
    ans = []
    for i in range(0 , n1):
        for j in range(0 , n2):
            if arr1[i] == arr2[j] and vis[j] == 0:
                ans.append(arr1[i])
                vis[j] = 1
                break
            if arr2[j] > arr1[i]:
                break
    return ans
# Time Complexity = O(N1 * N2) ----> O(N^2)
# Space Complexity = O(n2 + min(n1, n2)) --> O(N2)

def intersaction_Optimal(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    ans = []
    i , j = 0, 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
            j += 1
    return ans
# Time Complexity = O(N1 + N2) ----> O(2N)---> 0(N)
# Space Complexity = O(1)
print(intersaction_Optimal(arr1,arr2)) 
