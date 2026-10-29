def Decimal_to_Binary(num):
    result = ""
    while num != 0:
        if num %2 == 0:
            result += "0"
        else:
            result += "1"
        num = num//2
    result = result[::-1]
    return result

print(Decimal_to_Binary(8))

