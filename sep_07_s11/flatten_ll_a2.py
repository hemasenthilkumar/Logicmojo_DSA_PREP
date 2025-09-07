'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

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
        
    def getMiddle(self, head_):
        slow = head_
        fast = head_   
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def flatten(self, root):
        # code here
        #flatten = None
        #curr = root
        #while curr:
        #    flatten = self.merge(flatten, curr)
        #    curr = curr.next
        #return root
        if not root or root.next == None:
            return root
        
        # split into 2 halves
        mid = self.getMiddle(root)
        second = mid.next
        mid.next = None 
        
        # recursively flatten
        left  = self.flatten(root)
        right = self.flatten(second)
        return  self.merge(left, right)
        