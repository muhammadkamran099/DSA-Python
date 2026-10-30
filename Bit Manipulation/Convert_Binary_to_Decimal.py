def convert_to_decimal(st):
    decimal_number = 0
    index = len(st) - 1
    power = 0
    while index >= 0:
        num = int(st[index]) * (2**power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number

print(convert_to_decimal("1101"))