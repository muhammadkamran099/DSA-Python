
    
nums = [5, 9, 4]
result = []
total = 0
target = 9

def printSubSuquence(index, subseq, total):
    if total == target:
        result.append(subseq.copy())
        return
    elif total > target:
        return
    if index >= len(nums):
        return
    subseq.append(nums[index])
    sum = total + nums[index]
    printSubSuquence(index+1, subseq, sum)
    e = subseq.pop()
    sum -= e
    printSubSuquence(index+1, subseq, sum)

printSubSuquence(0, [], total)

print(result)

    