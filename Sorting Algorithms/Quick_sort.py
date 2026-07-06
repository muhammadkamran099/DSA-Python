nums = [4, 1, 7, 6, 3, 2, 8]

n = len(nums)
low = 0
high = n - 1

def partition(array, low, high):
    pivot = array[low]
    i = low
    j = high 
    while i < j:
        while array[i] <= pivot and i <= high - 1 :
            i += 1
        while array[j] > pivot and  j >= low + 1 :
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low]
    return j

def quick_sort(array, low, high):
    if low < high:
        p_index = partition(array, low, high)
        quick_sort(array, low, p_index - 1)
        quick_sort(array, p_index + 1, high)
        
quick_sort(nums, low, high)
print(nums)