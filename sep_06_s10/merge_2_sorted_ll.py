class Solution:
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
        
        #while l1:
        #    curr.next = l1
        #    curr = curr.next
        #    l1 = l1.next
        #while l2:
        #    curr.next = l2
        #    curr = curr.next
        #    l2 = l2.next
        if l1:
            curr.next = l1 
        if l2:
            curr.next = l2
            
        return head