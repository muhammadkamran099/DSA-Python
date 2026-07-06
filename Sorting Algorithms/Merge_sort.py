nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]

def merge_arr(left_arr,right_arr):
    i = 0
    j = 0
    n = len(left_arr) 
    m = len(right_arr)
    result = []
    while i <= n - 1 and j <= m - 1:
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    while i <= n - 1:
        result.append(left_arr[i])
        i += 1
    while j <= m - 1:
        result.append(right_arr[j])
        j += 1
    return result
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    mid = n // 2
    left_arr = arr[ : mid]
    right_arr = arr[mid : ]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_arr(left, right)
    
print(merge_sort(nums))
