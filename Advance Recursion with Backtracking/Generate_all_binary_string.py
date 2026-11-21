def generate_binary_strings(index, flag, numbers, result):
    if index >= len(numbers):
        result.append("".join(numbers))
        return
    numbers[index] = "0"
    generate_binary_strings(index+1, True, numbers, result)
    if flag == True:
        numbers[index] = "1"
        generate_binary_strings(index+1, False, numbers, result)
    return result
        
        
n = int(input("Enter a length of binary strings: "))
numbers = ["0"] * n
result = []

print(generate_binary_strings(0, True, numbers, result))
