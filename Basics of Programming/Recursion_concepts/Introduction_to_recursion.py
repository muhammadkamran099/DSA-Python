""" Recursion

A function that calls itself is called a recursive function.

Why Do We Use Recursion?

Recursion is useful for problems that can be broken into smaller, similar problems.


Important Terms

1. Base Case

The condition that stops the recursion.

Without a base case, recursion never ends.

2. Recursive Case

The part where the function calls itself. """


def print_numbers(n):
    if n == 0:          # Base case
        return

    print(n)
    print_numbers(n - 1)   # Recursive call

print_numbers(5)

