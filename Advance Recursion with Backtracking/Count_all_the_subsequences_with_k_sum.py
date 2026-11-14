nums = [5, 9, 4]
target = 9


def countSub(index, total):
    if total == target:
        return 1

    elif total > target:
        return 0

    if index >= len(nums):
        return 0

    pick = countSub(index + 1, total + nums[index])

    not_pick = countSub(index + 1, total)

    return pick + not_pick


print(countSub(0, 0))