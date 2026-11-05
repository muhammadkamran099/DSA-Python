a = 8
b = 6

print("Before Swapping")
print("a: ", a)
print("b: ", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After Swapping")
print("a: ", a)
print("b: ", b)