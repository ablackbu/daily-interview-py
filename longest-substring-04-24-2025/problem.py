import sys
import math

class Solution:
  def lengthOfLongestSubstring(self, s):
    max = 0
    length = 0
    prev = None
    while(len(s) > 0):
      length = length + 1 if prev is not s[0] else 0 #Increments or resets the current length 
      max = max if max > length else length #Updates max as length increments past it

      prev = s[0] #Remember the previous value
      s = s[1:] #Move the loop forward

    return max

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10