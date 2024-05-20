import math

def findPythagoreanTriplets(nums):

  for i, current in enumerate(nums):

    if(i+1 == len(nums)):
      break
    
    b_sq = math.pow(nums[i+1], 2)
    a_sq = math.pow(current, 2)
    c_target = math.sqrt(a_sq+b_sq)


    if(c_target in nums):
      return True
    

  return False

  #research more about pythat tripplet patterns
  #I would assume there is a nice pattern we could follow. 

print (findPythagoreanTriplets([3, 12, 5, 13]))
# True