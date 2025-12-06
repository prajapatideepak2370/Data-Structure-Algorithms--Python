# Find the average of array elements.

arr = [34,23,24,31,20,15,25]
avg = 0
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    avg = sum / len(arr)
print(avg)