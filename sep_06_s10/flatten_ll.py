'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

# TC: O(N*K) due to K times comparision -> N for the linked lists and K is the total items
# Optimized - we can do a merge sort in the lists itself

class Solution:
    
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        l1 = list1
        l2 = list2

        # assign the first head
        if l1.data <= l2.data:
            head = l1
            l1 = l1.bottom
        else:
            head=l2
            l2 = l2.bottom

        curr = head
        while l1 and l2:
            if l1.data < l2.data:
                curr.bottom = l1
                l1 = l1.bottom
            else:
                curr.bottom = l2
                l2 = l2.bottom
            curr = curr.bottom
        
        if l1:
            curr.bottom = l1 
        if l2:
            curr.bottom = l2
            
        return head
    
    def flatten(self, root):
        # code here
        flatten = None
        curr = root
        while curr:
            flatten = self.merge(flatten, curr)
            curr = curr.next
        return root