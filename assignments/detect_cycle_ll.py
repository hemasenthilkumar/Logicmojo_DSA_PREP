
from aug_31_s9.linked_list_basics import Node


def detect_cycle(head: Node):
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True 
    return False