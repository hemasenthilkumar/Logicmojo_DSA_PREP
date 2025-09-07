
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Insert cloned nodes in between
        curr = head
        while curr:
            temp = Node(curr.val)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next

        # Step 2: Assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and cloned lists
        curr = head
        cloned_head = head.next
        while curr:
            cloned = curr.next
            curr.next = cloned.next
            curr = curr.next
            if curr:
                cloned.next = curr.next

        return cloned_head


            
