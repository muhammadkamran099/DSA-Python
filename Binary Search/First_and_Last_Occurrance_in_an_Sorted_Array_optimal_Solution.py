def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb


def uper_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ub = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub


def first_LastOccurrance(nums, target):
    first = lower_bound(nums, target)

    if first == -1 or nums[first] != target:
        return -1, -1

    last = uper_bound(nums, target)

    if last == -1:
        last = len(nums) - 1
    else:
        last -= 1

    return first, last