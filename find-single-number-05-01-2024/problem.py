
def singleNumber(nums):


  while(len(nums) > 1):
    current = nums[0]
    try:
      nums[1:].index(current)
      nums.remove(current) #We have to do it twice this this only removes the first one it finds
      nums.remove(current)
    except Exception: #list.index errors when there it is not found - aka no mate for this
      return current
  
  return nums[0]

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
