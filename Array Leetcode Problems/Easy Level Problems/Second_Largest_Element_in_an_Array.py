nums = [55, 92, -97, 9, 3, 67]

largest = float('-inf')
s_largest = float('-inf')

for num in nums:
    if num > largest:
        s_largest = largest
        largest = num
    elif num > s_largest and num != largest:
        s_largest = num

print("Largest:", largest)
print("Second Largest:", s_largest)