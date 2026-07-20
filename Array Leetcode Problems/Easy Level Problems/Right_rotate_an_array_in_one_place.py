
"""Brute force"""

nums = [7, 5, 3, -2, -6, 8, 4]

n = len(nums)
nums[:] = nums[n-1:] + nums[0:n-1]

print(nums)