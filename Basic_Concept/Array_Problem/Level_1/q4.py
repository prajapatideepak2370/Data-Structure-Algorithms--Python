# Find the maximum element in an array. 

arr = [3,23,24,31,20,15,25]

mx = arr[0]
for num in arr:
    if num > mx:
        mx = num

maximum = max(arr)  # built-in 
print("The maximum element in an array: ",mx)

# Find the minimum element in an array. 

mn = arr[0]
for num in arr:
    if num < mn:
        mn = num
print("The minimum element in an array: ", mn)