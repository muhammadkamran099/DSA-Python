def lower_bound(nums: list[int], target: int) -> int:
    n = len(nums)
    lb = -1  # Set to -1 if no element >= target exists
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid        # Store potential lower bound index
            high = mid - 1  # Search left half for a smaller valid index
        else:
            low = mid + 1   # Search right half

    return lb