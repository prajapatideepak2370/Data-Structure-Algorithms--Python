# Count how many elements are even and odd. 

arr = [3,23,24,31,20,15,25]
odd = 0
even = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of Odd Value: ",odd)
print("Number of Even Value: ", even)