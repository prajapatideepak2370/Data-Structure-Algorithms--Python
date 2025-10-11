#Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the Divide and Conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array.
#Step 1:Divide: Divide the list or array recursively into two halves until it can no more be divided.
#Step 2:Conquer: Each subarray is sorted individually using the merge sort algorithm.
#Step 3:Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.
arr = [1, 2, 3, 4, 5, 1, 1, 3, 4, 5, 6, 7]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_sort = arr[:mid]
    right_sort =arr[mid:]
    left_sort = merge_sort(left_sort)
    right_sort = merge_sort(right_sort)
    return merge(left_sort, right_sort)

def merge(left, right):
    merged = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i<n and j<m:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < n:
        while i < n:
            merged.append(left[i])
            i += 1
    if j < m:
        while j < m:
            merged.append(right[j])
            j += 1
    return merged

print(merge_sort(arr))

# Time Complexity: O(nlogn) in all cases (best, average, and worst) because the array is always divided in half and then merged.
# Space Complexity: O(n) because we are using additional space to store the left and right subarrays during the merge process.