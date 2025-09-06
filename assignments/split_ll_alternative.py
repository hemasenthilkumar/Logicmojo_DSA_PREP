class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        head1 = head
        head2 = head.next
        curr1 = head
        curr2 = head.next
        while curr1 and curr2:
            temp = curr1.next
            curr1.next = temp.next
            if curr1.next:
                curr2.next = curr1.next.next
            curr1 = curr1.next
            curr2 = curr2.next
        return [head1, head2]