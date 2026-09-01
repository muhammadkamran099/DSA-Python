def rearrange_by_sign(nums):
    n = len(nums)
    result = [0] * n

    pos_idx = 0
    neg_idx = 1

    for num in nums:
        if num >= 0:
            result[pos_idx] = num
            pos_idx += 2
        else:
            result[neg_idx] = num
            neg_idx += 2

    return result


nums = [5, 10, -3, -1, -10, 4]

result = rearrange_by_sign(nums)

print(result)