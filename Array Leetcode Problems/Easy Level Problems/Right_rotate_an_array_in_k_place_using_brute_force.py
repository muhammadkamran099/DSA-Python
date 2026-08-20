def rotate_array(nums, k):
    n = len(nums)
    rotations = k % n

    for _ in range(rotations):
        e = nums.pop()
        nums.insert(0, e)

    return nums


nums = [3, 9, 5, 6, 7, 2]
k = 7

result = rotate_array(nums, k)
print(result)