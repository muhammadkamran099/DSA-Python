nums = [55, 92, -97, 9, 3, 67]
largest = float('inf')
s_largest = float('inf')
n = len(nums)
for i in range(1, n):
    if s_largest < largest:
        s_largest = largest
    largest = max(largest, nums[i])
    
    
print(largest)
print(s_largest)