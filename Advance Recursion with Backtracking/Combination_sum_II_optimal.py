def combination_sum_II(index: int, total: float, subset: list) -> list:
    '''
    returns a list that contains xyx
    first takes the value of s;daf
    process
    return
    '''
    
    if total == 0:
        result.append(subset.copy())
        return
    if total < 0:
        return
    if index >= len(nums):
        return
    for i in range(index, n):
        if i > index and nums[i] == nums[i - 1]:
            continue
        subset.append(nums[i])
        sum = total - nums[i]
        combination_sum_II(i + 1, sum, subset)
        subset.pop()
    return result
        
    
        
        
        
result = []
nums = [1, 1, 1, 2, 2, 3]
n = len(nums)
subset = []

print(combination_sum_II(0, 4, subset))