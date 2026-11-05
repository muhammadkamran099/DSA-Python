
# LEFT SHIFT (<<)
# Shifts bits to the LEFT.
# Adds zeros on the right.
# Each left shift by 1 multiplies by 2.

#   5 = 00000101
#       << 1
#       00001010 = 10


# RIGHT SHIFT (>>)
# Shifts bits to the RIGHT.
# For positive numbers, removes bits from the right.
# Each right shift by 1 divides by 2 (floor division).

#   5 = 00000101
#       >> 1
#       00000010 = 2


num1 = 13
num2 = 1

# Right shift operator
print(num1 >> num2)  

# Left shift operator
print(num1 << num2)  