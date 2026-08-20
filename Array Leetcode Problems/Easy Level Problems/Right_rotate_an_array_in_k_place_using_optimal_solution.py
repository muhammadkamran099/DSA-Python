def rotate_array(nums, k):
    n = len(nums)
    rotations = k % n

    nums[:] = nums[n - rotations:] + nums[:n - rotations]

    return nums


nums = [3, 9, 5, 6, 7, 2]
k = 7

result = rotate_array(nums, k)
print(result)