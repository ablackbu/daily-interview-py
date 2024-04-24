import sys
import math

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    
    #TODO add error handling for bad actors ?
    if l1 is None and l2 is None: 
      return None
    elif l1 is None:
      return l2
    elif l2 is None:
      return l1
    
    #We want to do this when everything is all good.
    newCarry = math.floor((l1.val + l2.val + c)/10)
    newVal = (l1.val + l2.val + c)% 10
    print(f"new val: {newVal} newCarry: {newCarry}")

    newNode = ListNode(newVal)
    newNode.next = self.addTwoNumbers(l1.next, l2.next, newCarry)
    return newNode 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(7)

result = Solution().addTwoNumbers(l1, l2)
print("result")
while result:
 print(result.val)
 result = result.next
# 7 0 8