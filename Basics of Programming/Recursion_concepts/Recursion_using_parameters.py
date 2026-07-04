""" Recursion Using Parameters

Sometimes we pass extra variables (parameters) to carry information.

Example: Sum from 1 to N """

def sum_numbers(i, total):
    if i < 1:
        print(total)
        return

    sum_numbers(i - 1, total + i)

sum_numbers(5, 0)