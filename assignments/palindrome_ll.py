"""
A1: Create a stack and insert the nodes
    pop the stack one by one and compare with original list
    return false if not equal else finally true
A2: Find middle, reverse and compare with original
"""


def reverse(head_node):
    prev = None
    curr = head_node
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev


def isPalindrome(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second_half = reverse(slow)
    curr = head
    curr2 = second_half
    while curr2:
        if curr.val != curr2.val:
            return False 
        curr = curr.next
        curr2 = curr2.next
    return True