""" Palindrome

A string that reads the same from both sides.

"""

def palindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return palindrome(s, left + 1, right - 1)

word = "madam"

print(palindrome(word, 0, len(word) - 1))