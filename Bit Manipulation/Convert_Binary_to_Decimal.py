def convert_to_decimal(n):
    if n == 0:
        return 0

    result = 0
    power = 0

    while n > 0:
        r = n % 10

        if r > 1:
            return "Invalid Binary Number"

        result += r * (2 ** power)
        n //= 10
        power += 1

    return result


print(convert_to_decimal(1011))