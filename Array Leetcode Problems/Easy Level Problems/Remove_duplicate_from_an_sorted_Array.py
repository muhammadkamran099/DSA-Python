""" Brute Force"""
# nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

# n = len(nums)
# freq_map = {}
# for i in range(0, n):
#     freq_map[nums[i]] = 0
# j = 0
# for k in freq_map:
#     nums[j] = k
#     j += 1
    
# print(nums)

"""Optimal Solution"""

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

def Remove_duplicate(nums):
    n = len(nums)

    if n == 1:
        return 1

    i = 0

    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    return i + 1

k = Remove_duplicate(nums)

print(k)
print(nums)
