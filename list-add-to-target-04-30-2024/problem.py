
def two_sum(list, k):
  for i, current in enumerate(list):
    for next in list[i+1:]:
      if(current+next == k):
        return True
  return False

print(two_sum([4,7,1,-3,2], 5))
# True
