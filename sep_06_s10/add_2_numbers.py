class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        a = l1
        b = l2
        carry = 0
        res = a.val + b.val
        if res >= 10:
            carry = 1
            res = res % 10
        result = ListNode(res)
        a = a.next
        b = b.next
        c = result
        while a or b:
            if not a:
                res = b.val + carry
            elif not b:
                res = a.val + carry
            else:
                res = a.val + b.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            new = ListNode(res)
            c.next = new
            c = c.next
            if a: 
                a = a.next
            if b:
                b = b.next 
        if carry == 1:
            c.next = ListNode(1)
        return result
