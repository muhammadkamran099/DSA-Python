nums = [4, 8, 9, 11]
result = []
target = 9
total = 0
def printSubSuquence(index, subseq, total):
    if total == target:
        result.append(subseq.copy())
        return
    elif total > target:
        return
    if index >= len(nums):
        return
    subseq.append(nums[index])
    total += nums[index]
    printSubSuquence(index + 1, subseq, total)
    subseq.pop()
    total -= nums[index]
    printSubSuquence(index + 1, subseq, total)
    
subseq = []
printSubSuquence(0, subseq, total)
print(result)


