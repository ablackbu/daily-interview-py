def check(lst):
  # Fill this in.

  changeCount = 0
  for i, current in enumerate(lst):
    #I'd rather use a for with an index here and do a i < len but don't know that syntax in python yet
    #We are at the end of the list
    if(i+1 >= len(lst)): 
      break
    
    next = lst[i+1]

    #print(f"current: {current} next {next} ")

    if(next < current):
      changeCount +=1
      if(changeCount>1): #Short circuit 
        break


  return changeCount<=1

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
#  False