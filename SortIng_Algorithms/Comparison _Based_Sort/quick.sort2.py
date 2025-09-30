# Last element as pivot algorithm

arr = [5,1,9,6,2,7,3,8,4]
print(arr)
def quickSort(arr, low, high):
        if low < high:
            if isSorted(arr, low, high): # Check if the subarray is already sorted
                return
            p_index = partition(arr, low, high)
            quickSort(arr, low, p_index - 1)
            quickSort(arr, p_index + 1, high)
            print(arr)
          
def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1        
    for j in range(low, high):
        if arr[j] <= pivot:   
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1
# isSorted function to check if the array is already sorted
def isSorted(arr, low, high):
    for i in range(low, high): 
        if arr[i] > arr[i + 1]:
            return False
    return True

n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)