def ceilFloor_binary(nums, target):
    low = 0
    high = len(nums) - 1
    ceil = -1
    floor = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return nums[mid], nums[mid]
        elif nums[mid] < target:
            floor = nums[mid]  
            low = mid + 1      
        else:
            ceil = nums[mid]   
            high = mid - 1     

    return ceil, floor

nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]
target = 2
print(ceilFloor_binary(nums, target))  