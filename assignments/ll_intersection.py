class Solution:
    def getIntersectionNode_a1(self, headA, headB):
        curr1 = headA
        curr2 = headB
        data = set()
        while curr1:
            data.add(curr1)
            curr1 = curr1.next
        
        while curr2:
            if curr2 in data:
                return curr2
            curr2 = curr2.next
        return None

    def getIntersectionNode_a2(self, headA, headB) :
        curr1 = headA
        curr2 = headB
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA 
        return curr1