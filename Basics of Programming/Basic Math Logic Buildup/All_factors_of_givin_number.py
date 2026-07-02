result = []

n = int(input("Enter a number: "))

num = n
for i in range(1, num // 2):
    if n%i == 0:
        result.append(i)
result.append(num)
print(result)
        