
class Solution:
    def detectCycle(self, head):
        # detect cycle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return 

    def detectCycle_a2(self, head):
        data = set()
        curr = head
        while curr:
            if curr in data:
                return curr
            data.add(curr)
            curr = curr.next
        return 
