def find_missing_number(nums):
    n = len(nums)

    for i in range(n + 1):
        if i not in nums:
            return i

    return -1


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

result = find_missing_number(nums)

print(result)