''' Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the
 list is repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list.'''
# Bubble Sort Algorithm Implementation of Average case & Wrost case
# how this is become a Average case & Wrost case becuase the outer loop is running from n-2 to 0 & inner loop is running from 0 to i+1 and they swap the elements if the left element is greater than the right element.
# If the array is already sorted then they also itterate through the array and compare the elements but they don't swap any elements.
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def bubble_sort(arr):
    for i in range(len(arr) - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort(arr))
# Time Complexity: O(n^2)
# Space Complexity: O(1)

#Best case Implementation of Bubble Sort
# In the best case, the array is already sorted, so the algorithm only needs to make one pass through the array to confirm that it is sorted. 
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def best_bubble_sort(arr2):
    for i in range(len(arr2) - 2, -1, -1):
        is_swapped = False
        for j in range(0, i + 1):
            if arr2[j] > arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
                is_swapped = True
        if not is_swapped:
            return
    return arr2
print(best_bubble_sort(arr2))

#This results in a time complexity of O(n).
# The space complexity remains O(1) since no additional space is used.