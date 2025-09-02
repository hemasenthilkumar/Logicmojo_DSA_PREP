"""
Middle of linked list
"""

from aug_31_s9.linked_list_basics import Node
from aug_31_s9.traversal import Traversal

def get_middle_a1(head: Node):
    curr = head
    size = 0
    while curr:
        curr = curr.next 
        size += 1

    mid = size//2
    curr = head
    counter = 0
    while curr and counter < mid :
        curr = curr.next
        counter += 1
    return curr
        

def get_middle_a2(head: Node):
    slow = head
    fast = head   
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

        
if __name__ == "__main__":

    # Linked List Formation
    head = Node(5)
    node1 = Node(6)
    head.nxt = node1 
    node2 = Node(4)
    node1.nxt = node2 
    node3 = Node(8)
    node2.nxt = node3
    node = get_middle_a1(head)
    tr = Traversal(node)
    tr.iterative_traversal()