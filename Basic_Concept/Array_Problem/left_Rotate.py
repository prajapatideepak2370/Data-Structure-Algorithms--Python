nums = [1,2,3,4,5,6,7]
k = int(input("Enter the number of rotations: "))
def rotate(nums, k):
    n = len(nums)
    k = k % n
    