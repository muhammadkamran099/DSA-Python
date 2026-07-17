nums = [55, 92, -97, 9, 3, 67]
largest = nums[0]
n = len(nums)
for i in range(1, n):
    largest = max(largest, nums[i])
    
print(largest)