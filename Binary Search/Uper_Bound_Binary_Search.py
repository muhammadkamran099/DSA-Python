def upper_bound(nums: list[int], target: int) -> int:
    n = len(nums)
    ub = -1  # Default if no element > target exists
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid        # Store potential upper bound index
            high = mid - 1  # Look left for an earlier valid index
        else:
            low = mid + 1   # Look right

    return ub