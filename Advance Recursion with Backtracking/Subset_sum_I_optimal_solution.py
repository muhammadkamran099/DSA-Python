def subset_sum_I(index, total, result):
    if index == len(numbers):
        result.append(total)
        return


    subset_sum_I(index + 1, total, result)

    subset_sum_I(index + 1, total + numbers[index], result)


numbers = [5, 9, 3]
result = []

subset_sum_I(0, 0, result)
print(result)