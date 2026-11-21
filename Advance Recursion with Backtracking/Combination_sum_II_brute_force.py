
def backtrack(subset, index, target, result, candidates):

    if target == 0:
        result.add(tuple(subset.copy()))
        return

    elif target < 0:
        return

    if index >= len(candidates):
        return

    # Pick
    subset.append(candidates[index])
    target -= candidates[index]

    backtrack(subset, index + 1, target, result, candidates)

    # Backtrack
    subset.pop()
    target += candidates[index]

    # Not Pick
    backtrack(subset, index + 1, target, result, candidates)


def combinationSum2(candidates, target):

    candidates.sort()
    result = set()

    backtrack([], 0, target, result, candidates)

    return [list(item) for item in result]


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

print(combinationSum2(candidates, target))
