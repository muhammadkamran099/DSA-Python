def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


def rotate_array(nums, k):

    n = len(nums)

    reverse(nums, n - k, n - 1)

    reverse(nums, 0, n - k - 1)

    reverse(nums, 0, n - 1)

    return nums


nums = [3, 9, 5, 6, 7, 2]
k = 3

result = rotate_array(nums, k)

print(result)