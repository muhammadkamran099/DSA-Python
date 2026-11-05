
# 1. AND (&)
# Returns 1 only when BOTH bits are 1.

#   5 = 0101
#   3 = 0011
#   --------
#       0001 = 1

# 2. OR (|)
# Returns 1 when AT LEAST ONE bit is 1.

#   5 = 0101
#   3 = 0011
#   --------
#       0111 = 7


# 3. XOR (^)
# Returns 1 when BOTH bits are DIFFERENT.
# Returns 0 when BOTH bits are SAME.

#   5 = 0101
#   3 = 0011
#   --------
#       0110 = 6



# 4. NOT (~)
# Flips all bits.
# In Python: ~n = -(n + 1)

#   5  = 00000101
#  ~5  = 11111010  (two's complement representation)
# Result = -6


# 5. LEFT SHIFT (<<)
# Shifts bits to the LEFT.
# Adds zeros on the right.
# Each left shift by 1 multiplies by 2.

#   5 = 00000101
#       << 1
#       00001010 = 10


# 6. RIGHT SHIFT (>>)
# Shifts bits to the RIGHT.
# For positive numbers, removes bits from the right.
# Each right shift by 1 divides by 2 (floor division).

#   5 = 00000101
#       >> 1
#       00000010 = 2

print(5 >> 1)  # 2
print(5 >> 2)  # 1


n1 = 3
n2 = 7
n3 = -13

print("AND", n1 & n2)

print("OR", n1 | n2)

print("XOR", n1 ^ n2)

print("NOT", ~n3)

