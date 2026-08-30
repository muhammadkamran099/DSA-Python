def longest_consecutive(nums):
    n = len(nums)
    max_count = 0

    for i in range(n):
        num = nums[i]
        count = 1

        while num + 1 in nums:
            count += 1
            num += 1

        max_count = max(max_count, count)

    return max_count


nums = [1, 99, 101, 98, 2, 5, 3, 100, 1]

result = longest_consecutive(nums)

print(result)