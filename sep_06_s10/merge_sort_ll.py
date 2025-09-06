"""
Find middle --> Need to use logic where it returns 1nd node in case of even numbers
 -- for this just make fast.next.next is also not null -> it will return the first node
SPlit
Merge
"""

class Solution:

    def getMiddle(self, head_):
        slow = head_
        fast = head_   
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        l1 = list1
        l2 = list2

        # assign the first head
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head=l2
            l2 = l2.next

        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1 
        if l2:
            curr.next = l2
            
        return head

    def sortList(self, head):
        if head==None or head.next==None:
            return head
        mid = self.getMiddle(head)
        # split into halves
        mid_next = mid.next
        mid.next = None

        first = self.sortList(head)
        second = self.sortList(mid_next)

        return self.mergeTwoLists(first, second)
        