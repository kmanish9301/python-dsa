import math

# nums1 = [-1, 0, 3, 5 ,9, 12]
# target1 = 9

nums2 = [-1,0,3,5,9,12]
target2 = 2


def binary_search(nums, target):
    start = 0
    end = len(nums) -1

    while start <= end:
        middle = math.floor((start+end)/2)
        if target == nums[middle]:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return -1

print(binary_search(nums2, target2))