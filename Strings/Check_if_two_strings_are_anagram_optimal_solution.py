def anagramString(s, t):
    n = len(s)
    ch_freq = {}
    if len(s) != len(t):
        return False
    for ch in s:
        ch_freq[ch] = ch_freq.get(ch, 0) + 1
    for ch in t:
        if ch not in ch_freq:
            return False
        else:
            if ch_freq[ch] == 0:
                return False
            else:
                ch_freq[ch] -= 1
    return True  

s = "anagram"
t = "nagaram"

print(anagramString(s, t))