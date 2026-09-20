

def largest_Odd_number(nums):
    n = len(nums)
    for i in range(n -1, -1, -1):
        if int(nums[i]) % 2 == 1:
            return nums[0: i + 1]
    return ""

nums = "68329668420"

result = largest_Odd_number(nums)
print(result)
        