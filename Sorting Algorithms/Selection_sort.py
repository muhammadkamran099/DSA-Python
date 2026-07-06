nums = [ 3, 4, 5, 6, 8, 9, 10, 7,  1]
n = len(nums)
for i in range(0, n):
    min_index = i
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
    
print(nums)