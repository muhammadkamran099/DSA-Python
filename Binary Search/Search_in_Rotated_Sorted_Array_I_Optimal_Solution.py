def search_rotated_sorted_array(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

nums = [17, 18, 20 , 1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16]
target = 4
result = search_rotated_sorted_array(nums, target)
print(result)