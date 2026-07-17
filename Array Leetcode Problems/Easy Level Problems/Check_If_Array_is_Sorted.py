nums = [5, 6, 7, 9, 11, 13]

n = len(nums)

is_sorted = True

for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

print(is_sorted)