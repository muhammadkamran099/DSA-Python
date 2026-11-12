
    
nums = [4, 8, 5]
result = []

def printSubSuquence(index, subseq):
    if index >= len(nums):
        result.append(subseq.copy())
        return
    subseq.append(nums[index])
    printSubSuquence(index + 1, subseq)
    subseq.pop()
    printSubSuquence(index + 1, subseq)
    
subseq = []
printSubSuquence(0, subseq)
print(result)


    