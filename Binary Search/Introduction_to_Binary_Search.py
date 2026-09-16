
def binarySearch(nums, target):
    n = len(nums)
    st = 0
    end = n - 1
    while st <= end:
        mid = ( st + end ) // 2
        if target == nums[mid]:
            return mid 
        elif target > nums[mid]:
            st = mid + 1
            mid = ( st + end ) // 2
        else:
            end = mid - 1
            mid = ( st + end ) // 2
    return -1 

nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = 6

result = binarySearch(nums, target)
print(result)