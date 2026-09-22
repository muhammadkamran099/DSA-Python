def checkAnagramString(s, t):
    if len(s) != len(t):
        return False

    sort_s = sorted(s)
    sort_t = sorted(t)

    return sort_s == sort_t


s = "anagram"
t = "nagaram"

print(checkAnagramString(s, t))
