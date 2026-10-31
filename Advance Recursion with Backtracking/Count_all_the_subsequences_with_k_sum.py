nums = [5, 9, 4]
target = 9

def countSubsequence(index, total):
    if total == target:
        return 1
    if total > target:
        return 0
    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = countSubsequence(index + 1, sum)
    sum = total
    not_pick = countSubsequence(index + 1, sum)

    return pick + not_pick

print(countSubsequence(0, 0))