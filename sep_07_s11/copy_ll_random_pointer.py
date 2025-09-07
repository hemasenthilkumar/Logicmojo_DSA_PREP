
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        # while creating a node, create a map also {key=node, value=Node}
        if not head:
            return head
        head1 = Node(head.val)
        curr2 = head1
        cache = {head: head1}
        curr = head.next
        while curr:
            temp = Node(curr.val)
            curr2.next = temp
            cache[curr] = temp
            curr = curr.next
            curr2 = curr2.next
        

        curr = head
        curr2 = head1
        """
        while curr:
            curr2.random = cache.get(curr.random)
            curr2 = curr2.next
            curr = curr.next
        """
        for k,v in cache.items():
            v.random = cache.get(k.random)
        return head1