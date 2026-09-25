def search_rotated_sorted_array(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    is_true = False
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            is_true = True
            return is_true
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
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

    return is_true