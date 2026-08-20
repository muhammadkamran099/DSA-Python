def find_missing_number(nums):
    n = len(nums)

    freq = {}

    for i in range(n + 1):
        freq[i] = 0

    for num in nums:
        freq[num] = 1

    for k, v in freq.items():
        if v == 0:
            return k

    return -1


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

result = find_missing_number(nums)

print(result)