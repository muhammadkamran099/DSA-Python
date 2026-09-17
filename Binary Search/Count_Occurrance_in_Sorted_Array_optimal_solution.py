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
    ub = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


def countOccurrance(nums, target):
    count = uper_bound(nums, target) - lower_bound(nums, target)

    if count == 0:
        return -1

    return count

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 10
result = countOccurrance(nums, target)
print(result)