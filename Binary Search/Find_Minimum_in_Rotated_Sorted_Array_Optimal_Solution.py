def minRotatedSorted(nums):
    n = len(nums)
    low = 0
    high = n - 1
    mini = float("inf")

    while low <= high:
        if nums[low] <= nums[high]:
            mini = min(mini, nums[low])
            break

        mid = (low + high) // 2

        if nums[high] > nums[mid]:
            mini = min(mini, nums[mid])
            high = mid - 1
        else:
            mini = min(mini, nums[low])
            low = mid + 1

    return mini