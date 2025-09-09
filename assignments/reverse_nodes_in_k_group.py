#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy

        while pointer:
            leftside = pointer
            for _ in range(k):
                pointer = pointer.next
                if not pointer:
                    break
            if not pointer:
                break
            # pointer -> last node of current group
            # before reverse 2 things to saved
            future_last = leftside.next
            # reverse
            curr = future_last
            prev = pointer.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # prev -> pointing to first node of the group
            leftside.next = prev # new node of the group
            pointer = future_last
        return dummy.next