
from linked_list_basics import Node
from traversal import Traversal

class Reversal:

    @staticmethod
    def reverse_iterative(head_node: Node):
        prev = None
        curr = head_node 
        while curr:
            temp = curr.nxt
            curr.nxt = prev 
            prev = curr 
            curr = temp 
            
        return prev
    
    @staticmethod
    def recurse(prev: Node, curr: Node):
        if not curr:
            return prev
        temp = curr.nxt
        curr.nxt = prev
        return Reversal.recurse(curr, temp)
    
    @staticmethod
    def reverse_recursive(head_node: Node):
        return Reversal.recurse(None, head_node)
    
if __name__ == "__main__":

    # Linked List Formation
    head = Node(5)
    node1 = Node(6)
    head.nxt = node1 
    node2 = Node(4)
    node1.nxt = node2 
    node3 = Node(8)
    node2.nxt = node3
    tr = Traversal(head)
    tr.iterative_traversal()
    head = Reversal.reverse_recursive(head)
    tr = Traversal(head)
    tr.iterative_traversal()