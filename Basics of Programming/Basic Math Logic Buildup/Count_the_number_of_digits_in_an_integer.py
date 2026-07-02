n = 5768
num = n
def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count
print(count_digits(num))