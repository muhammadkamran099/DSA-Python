def upper_bound(nums: list[int], target: int) -> int:
    n = len(nums)
    ub = -1  
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid        
            high = mid - 1  
        else:
            low = mid + 1   

    return ub