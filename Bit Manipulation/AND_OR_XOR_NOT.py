
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
# check if number is negative( if last 31th bit 1 then its negative number if 0 then its positive number) then takes two's compliment if not negative then stop


#   5  = 00000101
#  ~5  = 11111010  (two's complement representation)
# Result = -6



print(5 >> 1)  # 2
print(5 >> 2)  # 1


n1 = 3
n2 = 7
n3 = -13

print("AND", n1 & n2)

print("OR", n1 | n2)

print("XOR", n1 ^ n2)

print("NOT", ~n3)

