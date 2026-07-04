""" Parameterized Recursion

The answer is carried using parameters.

Example """

def sum_numbers(i, total):
    if i < 1:
        print(total)
        return

    sum_numbers(i - 1, total + i)

sum_numbers(5, 0)

""" Functional Recursion

The function returns the answer.

Example """

def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)

print(sum_numbers(5))

 
""" Difference

Parameterized	                Functional

Uses extra parameter	        Uses return value
Doesn't return answer	        Returns answer
Carries answer forward	        Builds answer while returning """