# count consecutive ones optimal solution
def max_consecutive_ones(nums):
    count = 0
    max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0

    max_count = max(max_count, count)

    return max_count


nums = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1]

result = max_consecutive_ones(nums)

print(result)