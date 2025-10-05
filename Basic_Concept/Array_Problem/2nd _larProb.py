arr = [55, -67, - 56, -98, -88, -24, -72, -90, - 66]
def secLargest(arr):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(arr)
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    for i in range(n):
        if arr[i] != largest and arr[i] > s_largest:
            s_largest = arr[i]
    if s_largest == float("-inf"):
        return None  # or raise an Exception if no second largest exists
    return s_largest

print(secLargest(arr))