class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    currentNode = head
    previousNode = None
    while currentNode is not None:
      #Need to store the next before we overwrite it
      nextNode = currentNode.next

      #Actual reversing bit
      currentNode.next = previousNode
      
      #Setup the next iteration
      previousNode = currentNode
      currentNode = nextNode

    return currentNode

  # Recursive Solution      
  def reverseRecursively(self, head):

    print(f" val: {head.val} next: {head.next}")

    if(head is None or head.next is None):
      #Base  condition makes sense
      return head
    
    rest = self.reverseRecursively(head.next)

    # Don't think I grasp this atm ... WTF ?
    # Come back later because this still doesn't click right now 
    # Put first element at the end
    head.next.next = head
    head.next = None

    #Since everything is now reversed we are good to return it
    return rest
   

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4