def rearrange_by_sign(nums):
    pos = []
    neg = []

    for num in nums:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    for i in range(len(pos)):
        nums[i * 2] = pos[i]
        nums[i * 2 + 1] = neg[i]

    return nums


nums = [5, 10, -3, -1, -10, 6]

result = rearrange_by_sign(nums)

print(result)