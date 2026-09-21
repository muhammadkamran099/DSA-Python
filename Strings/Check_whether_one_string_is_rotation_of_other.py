def checkStringRotation(s, goal):
    if len(s) != len(goal):
        return False

    curr_s = s
    n = len(curr_s)

    for i in range(n):
        if curr_s == goal:
            return True
        curr_s = curr_s[-1] + curr_s[0:-1]

    return False


s = "abcde"
goal = "cdeab"

print(checkStringRotation(s, goal))
