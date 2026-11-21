
def generate_paranthesis(index, total, brackets, result):
    if index >= len(brackets):
        if total == 0:
            result.append("".join(brackets))
        return
    if total > len(brackets) // 2:
        return
    elif total < 0:
        return
    brackets[index] = "("
    sum = total + 1
    generate_paranthesis(index + 1, sum, brackets, result)
    brackets[index] = ")"
    sum = total - 1
    generate_paranthesis(index + 1, sum, brackets, result)
    return result
n = int(input("Enter a length of paranthesis: "))
brackets = [""] * (n*2)
result = []

print(generate_paranthesis(0, 0, brackets, result))