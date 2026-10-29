def decimal_to_binary(num):
    if num == 0:
        return "0"

    is_negative = num < 0
    num = abs(num)
    result = ""

    while num != 0:
        if num % 2 == 0:
            result += "0"
        else:
            result += "1"

        num = num // 2

    result = result[::-1]

    if is_negative:
        result = "-" + result

    return result


print(decimal_to_binary(8))    
