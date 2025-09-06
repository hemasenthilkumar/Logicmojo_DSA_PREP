class Solution:
    
    def get_size(self, node):
        curr = node
        size = 0
        while curr:
            curr = curr.next
            size += 1
        return size

    def rotateRight(self, head, k: int):
        size = self.get_size(head)
        if size == 0 or k==0:
            return head
        k =  k % size
        if k == 0:
            return head
        # got to k-1th node from last
        moves = size - k -1 
        curr = head
        for _ in range(moves):
            curr = curr.next
        second = curr.next
        first = head
        curr.next = None

        s_curr = second
        # reach end of the second list
        while s_curr.next:
            s_curr = s_curr.next
        s_curr.next = first

        return second
