

# Frequency means how many times an element appears in a list or string.


# A dictionary stores data as:

# Key → Value
# For frequency counting:
# Key = Element
# Value = Number of times it appears


arr = [1, 2, 2, 3, 3, 3]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)