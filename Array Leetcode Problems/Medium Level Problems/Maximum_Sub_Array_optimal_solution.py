def max_sub_array(nums):
    total = 0
    max_sum = float("-inf")

    for num in nums:
        total += num
        max_sum = max(max_sum, total)

        if total < 0:
            total = 0

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_sub_array(nums)

print(result)