num = int(input("Enter a number: "))

original = num
temp = num
count = 0
total = 0

while temp > 0:
    count += 1
    temp = temp // 10

temp = original

while temp > 0:
    digit = temp % 10
    total = total + (digit ** count)
    temp = temp // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")