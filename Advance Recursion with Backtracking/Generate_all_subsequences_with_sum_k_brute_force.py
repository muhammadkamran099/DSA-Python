nums = [4, 8, 9, 11]
result = []
target = 9
def printSubSuquence(index, subseq):
    if index >= len(nums):
        if sum(subseq) == target:
            result.append(subseq.copy())
        return
    subseq.append(nums[index])
    printSubSuquence(index + 1, subseq)
    subseq.pop()
    printSubSuquence(index + 1, subseq)
    
subseq = []
printSubSuquence(0, subseq)
print(result)


