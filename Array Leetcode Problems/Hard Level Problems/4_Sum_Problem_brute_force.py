def four_sum(nums, target):
    n = len(nums)

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        return i, j, k, l

    return -1

nums = [1, 0, -1, 0, 2, -2, 5, 9] 
target = 0 
result = four_sum(nums, target) 
print(result)