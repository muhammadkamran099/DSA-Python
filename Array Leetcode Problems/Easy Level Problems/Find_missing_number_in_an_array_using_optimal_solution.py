# optimal_solution
def sum_n(n):

    return n * (n + 1) // 2


def find_missing_number(nums):

    n = len(nums)

    expected_sum = sum_n(n)

    actual_sum = 0

    for num in nums:
        actual_sum += num

    return expected_sum - actual_sum


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

result = find_missing_number(nums)

print(result)