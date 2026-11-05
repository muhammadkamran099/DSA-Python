a = 13
b = 12

ans = a ^ b
count = 0
for i in range(0, 32):
    if ans & ( 1 << i ) != 0:
        count += 1

print(count)

