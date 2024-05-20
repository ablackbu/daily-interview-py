class Solution:

  openCloseDist = {
    '(': ')',
    ')': '(',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '[',
  }

  def isClosing(self, s):
    return s in [']', '}', ')']

  def isValid(self, s):
    stack = []

    for element in s:
      print(stack)
      if self.isClosing(element):
        if stack.pop() is not self.openCloseDist[element]:
          return False
      else:
        stack.append(element)
      

    # Fill this in.
    return len(stack) == 0

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))