nums = [1, 2, 3]

n = len(nums)

sub_sets = 1 << n
result = []

for num in range(0, sub_sets):
    list = []
    for i in range(0, n):
        if num & ( 1 << i ) != 0:
            list.append(nums[i])
    result.append(list)
    
print(result)