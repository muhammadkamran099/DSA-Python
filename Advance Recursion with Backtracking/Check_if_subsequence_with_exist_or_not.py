
    
nums = [5, 9, 4]
result = []
total = 0
target = 9

def printSubSuquence(index, subseq, total):
    if total == target:
        return True
    elif total > target:
        return False
    if index >= len(nums):
        return False
    subseq.append(nums[index])
    sum = total + nums[index]
    pick = printSubSuquence(index+1, subseq, sum)
    if pick == True:
        return True
    e = subseq.pop()
    sum -= e
    not_pick = printSubSuquence(index+1, subseq, sum)
    return not_pick

print(printSubSuquence(0, [], 0))



    