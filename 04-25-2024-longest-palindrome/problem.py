from itertools import combinations

class Solution: 
    def longestPalindrome(self, s):

      #If we have a short string we just bail
      if(len(s) <= 1):
         return len(s)
      
      max = ""
      for ss in self.getAllSubStrings(s):
         isPalindrome = self.isPalindrome(ss)
         max = ss if isPalindrome and len(max) < len(ss) else max #Updates max with a new substring increments past it
      
      return max
    
    def isPalindrome(self, s):
       if(len(s) <=1):
          return True
       possibleP =  s[0] is s[len(s)-1]
       return possibleP and self.isPalindrome(s[1:len(s)-1])
    
    def getAllSubStrings(self, s): 
      #I want to to understand this better. I think it'll make more sense when I better understand range
      #https://docs.python.org/3.8/library/stdtypes.html#typesseq
       return [s[x:y] for x, y in combinations(range(len(s) + 1 ), r = 2 )]
      
       

        
# Test program
s = "tracecars"
print(Solution().longestPalindrome(s))
# racecar

print(str(Solution().longestPalindrome("banana")))
#anana

print(str(Solution().longestPalindrome("million")))
#illi