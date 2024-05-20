def sortNums(nums):
  dict = {}

  for x in nums:
    if(dict[x] is None):
      dict[x] = 1  
    else:
      #dict[x] += 1
      dict[x] = dict[x]  + 1

  print(dict)
  
  return 0

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]