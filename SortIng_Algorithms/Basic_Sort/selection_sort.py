# Selection sort is a simple sorting algorithm that divides the input list into two parts: a sorted and an unsorted part. It repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the end of the sorted part.
# The algorithm maintains two subarrays within the original array: the left subarray which is sorted and the right subarray which is unsorted. Initially, the sorted subarray is empty and the unsorted subarray contains all the elements. The algorithm iteratively selects the smallest element from the unsorted subarray and swaps it with the leftmost unsorted element, effectively growing the sorted subarray by one element.
# The process continues until the entire array is sorted.
# Selection sort is not a stable sorting algorithm because it may change the relative order of equal elements. For example, if two equal elements are present in the array, their order may be changed after sorting.

nums = [7, 5, 2, 4, 3, 9, 1, 6, 8]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  
    return arr
print(selection_sort(nums))


'''
Dry Run:
Iteration 1:
i = 0, min_index = 0
j = 1, arr[j] = 5 < arr[min_index] = 7, min_index = 1
j = 2, arr[j] = 2 < arr[min_index] = 5, min_index = 2
j = 3, arr[j] = 4 < arr[min_index] = 2, min_index = 2
j = 4, arr[j] = 3 < arr[min_index] = 2, min_index = 2
j = 5, arr[j] = 9 < arr[min_index] = 2, min_index = 2
j = 6, arr[j] = 1 < arr[min_index] = 2, min_index = 6
Swap arr[i] and arr[min_index]: arr[0], arr[6] = arr[6], arr[0]
Array after iteration 1: [1, 5, 2, 4, 3, 9, 7, 6, 8]
Doing this for all iterations, we get the final sorted array:
Array after iteration : [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# The time complexity of selection sort is O(n^2) in all cases (best, average, and worst) because it always involves two nested loops. 
# The space complexity is O(1) since it only requires a constant amount of additional memory space.
