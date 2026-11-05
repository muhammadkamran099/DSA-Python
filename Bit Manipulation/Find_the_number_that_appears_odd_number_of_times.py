nums = [2, 2, 3, 4, 4, 6, 6, 8, 8]

n = len(nums)
ans = 0
for i in range(n):
    ans = ans ^ nums[i]
    
print(ans)