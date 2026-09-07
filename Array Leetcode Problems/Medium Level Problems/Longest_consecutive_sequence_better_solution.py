def longest_consecutive(nums):
    nums.sort()
    
    count = 0
    last_smaller = float("-inf")
    longest = 0

    for num in nums:
        if num == last_smaller + 1:
            count += 1
            last_smaller = num
        elif num == last_smaller:
            continue
        else:
            count = 1
            last_smaller = num

        longest = max(longest, count)

    return longest


nums = [1, 99, 101, 98, 2, 5, 3, 100, 1]

result = longest_consecutive(nums)

print(result)