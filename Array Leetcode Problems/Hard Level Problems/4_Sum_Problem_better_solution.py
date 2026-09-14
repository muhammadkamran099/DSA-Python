
def four_sum(nums, target):
    n = len(nums)
    my_set = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            my_hash = set()
            for k in range(j + 1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in my_hash:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    my_set.add(tuple(temp))
                my_hash.add(nums[k])
    return my_set
                    


nums = [1, 0, -1, 0, 2, -2, 5, 9]
target = 0 
result = four_sum(nums, target)
print(result)
