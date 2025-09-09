def reverse(head):
    curr = head 
    prev = None 
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def get_mid(head):
    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def rearrangeList(head):
    # Write your code here
    first = head
    mid = get_mid(head)
    second = reverse(mid.next)
    mid.next = None
    
    while second:
        temp = first.next
        temp2 = second.next
        first.next = second
        second.next = temp
        first = temp
        second =  temp2
    
    return head