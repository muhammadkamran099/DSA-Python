def max_sub_array(nums):
    n = len(nums)
    max_sum = float("-inf")

    for i in range(n):
        total = 0

        for j in range(i, n):
            total += nums[j]
            max_sum = max(max_sum, total)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_sub_array(nums)

print(result)