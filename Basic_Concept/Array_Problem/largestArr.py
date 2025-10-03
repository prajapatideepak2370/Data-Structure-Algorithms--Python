arr = [-45, -35, -87, -34 , -99, -23, -67, -1]

def find_largest(arr):
    if len(arr) == 0:
        return None # Handle empty array case
    largest = float("-inf") # Initialize to the smallest possible value in Negative infinity numbers
    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

print("Largest element is:",find_largest(arr))