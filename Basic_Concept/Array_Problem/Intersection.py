nums1 = [1,2,2,1]
nums2 = [2,2]


def intersection_arr(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result = set1.intersection(set2)
    return list(result)
# TC = O(N1 + N2) SC= O(min(N1, N2))



def intersection_dict(nums1, nums2):
    count = {}
    for num in nums1:
        count[num] = 1
    result = []
    for num in nums2:
        if num in count:
            result.append(num)
            del count[num]
    return result
print(intersection_dict(nums1, nums2))
# Time Complexity = O(N1 + N2)
# Space Complexity = O(N1)


def intersection_two_pointer(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# TC= O(NlogN + MlogM) SC=O(1)