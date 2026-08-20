def find_target(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return target, i

    return -1, -1


nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]
target = 4

result = find_target(nums, target)

print(result)