
# Brute Force 

def move_zeros(nums):
    
    n = len(nums)

    temp = []

    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])

    tn = len(temp)

    for i in range(tn):
        nums[i] = temp[i]

    for i in range(tn, n):
        nums[i] = 0

    return nums


nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]

result = move_zeros(nums)

print(result)