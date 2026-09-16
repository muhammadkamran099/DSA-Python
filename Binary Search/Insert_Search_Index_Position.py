def insertSearch(nums, target):
  n = len(nums)
  low = 0
  high = n -1
  si = n
  while low <= high:
    mids = ( low + high ) // 2
    if nums[mids] >= target:
      si = mids
      high = mids - 1
    else:
      low = mids + 1
  return si
    


nums = [1, 3, 4, 5, 6, 7, 9, 11, 14, 15, 17, 20]
target = 14
result = insertSearch(nums, target)
print(result)


