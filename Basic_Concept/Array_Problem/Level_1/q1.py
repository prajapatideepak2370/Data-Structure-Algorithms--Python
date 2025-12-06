#Input n and take n integers into an array, print them.

arr = []
n = int(input("Enter the N: "))
for i in range(0, n):
    value = int(input("Enter the number: "))
    arr.append(value)
print("Array: ", arr)


# Method 2 
arr1 = list(map(int, input("Enter elements separated by space: ").split()))
print("Your array is:", arr1)
