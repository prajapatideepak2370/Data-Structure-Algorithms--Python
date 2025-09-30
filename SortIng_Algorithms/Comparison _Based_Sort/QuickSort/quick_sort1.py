#QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
'''
It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.
There are mainly three steps in the algorithm:
1--> Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
2--> Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
3--> Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
4--> Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted.
'''

# First element as the pivot algorithm
arr = [4,1,3,6,2,7,9,8,5]
n = len(arr)
def partition(arr, low, high):
    pivot = arr[low]
    i = low 
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sorted(arr, low, high):
        if low < high:
            p_indx = partition(arr, low, high)
            quick_sorted(arr, low, p_indx-1)
            quick_sorted(arr, p_indx+1, high)

quick_sorted(arr, 0, n-1)
print(arr)
# Time Complexity: O(n log n) on Average and Best case, O(n^2) in the worst case.
# Space Complexity: O(1)
