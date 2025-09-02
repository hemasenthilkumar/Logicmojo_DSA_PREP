class Solution:
    def reverse(self, head):
        # code here
        if not head:
            return None 
        
        curr = head
        new_head = None 
        
        while curr:
            curr.next, curr.prev = curr.prev, curr.next
            new_head = curr 
            curr = curr.prev
        
        return new_head
            