
def Largest_Common_Prefix(strs):
    s = ""
    base = strs[0]
    for i in range(0, len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
                return s
        s += base[i]
    return s
    



strs = ["flower", "flow", "flight"]
result = Largest_Common_Prefix(strs)
print(result)
