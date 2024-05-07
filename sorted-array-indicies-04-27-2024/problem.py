

class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    min = -1
    max = -1
    
    for i, item in enumerate(arr):
      
      if(item < target):  #The array is sorted so we can move to the next when we are under
        continue
      elif(item > target): #The array is sorted so we can end if we are over
        break
      else: #We know we have hit the target
          max = i
          if(min == -1): #Only update min when its the first occurance
            min = i
      
    return [min, max]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]


# Test program 
arr = [1,3,3,5,7,8,9,9,9,15] 
x = 9
print(Solution().getRange(arr, x))
# [6, 8]


# Test program 
arr = [100, 150, 150, 153] 
x = 150
print(Solution().getRange(arr, x))
# [1, 2]

# Test program 
arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
# [-1, -1]