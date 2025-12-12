nums = [1,2,3, 3]
n = len(nums)
hash_list = [0] * n
for num in nums:
    hash_list[num] += 1
# print(hash_list)
for i in hash_list:
    if hash_list[i] <= 2:
        print(True)
        break
    else:
        print(False)