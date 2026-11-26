def solve(index, subset):
    if index >= len(digits):
        result.append("".join(subset))
        return
    for ch in char_map[digits[index]]:
        subset.append(ch)
        solve(index + 1, subset)
        subset.pop()
    return result
        
        
index = 0 
digits = "46"
result = []
char_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

print(solve(index, []))