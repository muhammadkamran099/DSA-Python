def combination_sum(index, total, numbers, result, target):
    if total > target:
        return
    if total == target:
        result.append(my_list.copy())
        return
    if index >= len(numbers):
        return
    my_list.append(numbers[index])
    sum = total + numbers[index]
    combination_sum(index, sum, numbers, result, target)
    my_list.pop()
    sum = total
    combination_sum(index + 1, sum, numbers, result, target)
    return result
    
    
    
    
    
my_list = []
numbers = [2, 3, 6, 7]
result = []
target = 7

print(combination_sum(0, 0, numbers, result, target))
