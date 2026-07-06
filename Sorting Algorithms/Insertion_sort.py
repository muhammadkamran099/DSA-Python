# Insertion Sort
nums = [ 3, 4, 5, 6, 8, 9, 10, 7,  1]
n = len(nums)
for i in range(1, n):
    key = nums[i]
    j = i-1
    while j>= 0 and key < nums[j]:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key
    
print(nums)