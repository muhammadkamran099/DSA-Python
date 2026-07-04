"""

Fibonacci Series
0 1 1 2 3 5 8 13 ...

Rule

Current Number = Previous Number + Second Previous Number

"""


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))