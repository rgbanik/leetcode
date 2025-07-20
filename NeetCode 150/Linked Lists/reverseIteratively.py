"""
Given the head of a linked list, reverse it, and return the new head.
Not being able to do this is embarrassing.
"""

# Each node of the linked list is an instance of the Node class,
# and it contains a value as well as a reference to the next node in the list
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList_iterative(self, node):
    pass



if __name__ == "__main__":

    # First, let's create a list containing values from one to five
    head = Node(1)

    curr = head
    for i in range(2,6):
        newNode = Node(i)
        curr.next = newNode
        curr = curr.next

    # Now let's print out the values in the list
    print("Printing created list:")
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next

    # Now, let's reverse the list, and then we'll print it out
    print("Reversing list now:")
    newhead = reverseList_iterative(head)
    while newhead is not None:
        print(newhead.val)
        newhead = newhead.next