"""
A1: Find the diff between 2 LL
    Iterate the diff
    iterate both now and move untill they dont meet
"""

class Solution:

    def size(self, head):
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        return count

    def getIntersectionNode(self, headA, headB) :
        sizeA = self.size(headA)
        sizeB = self.size(headB)
        diff = abs(sizeA-sizeB)
        curr1 = headA
        curr2 = headB
        if sizeB > sizeA:
            for _ in range(diff):
                curr2 = curr2.next
        else:
            for _ in range(diff):
                curr1 = curr1.next            
        # moved both of them, now need to iterate
        while (curr1 and curr2) and curr1 != curr2:
            curr1= curr1.next
            curr2 = curr2.next
        
        return curr1