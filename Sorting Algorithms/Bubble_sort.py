nums = [ 3, 4, 5, 6, 8, 9, 10, 7,  1]
n = len(nums)
for i in range(1, n):
    for j in range(n-1, i-1, -1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]

print(nums)