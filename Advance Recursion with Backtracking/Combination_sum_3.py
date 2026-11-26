def solve(last, total, subset, k, n, result):
        if total == n and len(subset) == k:
            result.append(subset.copy())
            return

        if total > n or len(subset) >= k:
            return

        for i in range(last, 10):
            subset.append(i)
            sum = total + i
            solve(i + 1, sum, subset, k, n, result)
            subset.pop()


result = []
k = 3
n = 7
print(solve(1, 0, [], k, n, result))