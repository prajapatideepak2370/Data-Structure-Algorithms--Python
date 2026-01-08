# Find the first occurrence of a given number.
arr = [4, 2, 7, 2, 9, 2]
target = int(input("Enter the number: "))
found = False
for i in range(0, len(arr)):
    if arr[i] == target:
        print("Taregt found at index:", i)
        found = True
        break
if not found:
    print("Target is not found")

# Find the last occurrence of a given number. 
nums = [4, 6, 7, 6, 9, 6]
target = int(input("Enter the number: "))
last_index = -1
for i in range(0, len(nums)):
    if nums[i] == target:
        last_index = i
if last_index != -1:
    print("Taregt found at index:", last_index)
else:
    print("Target is not found")