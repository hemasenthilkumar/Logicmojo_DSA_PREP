"""
Insertion in Linked List 

# Insert at the head node O(1)
1. create linkage between new node & the head node
2. Update the head node

# Insert at the end O(N)
-- Very easy
1. Create a new node
2. Traverse & get the last node
3. Link the last node to the new node

# Insert any position

1. Reach at pos by traversing
2. Save the node's next to some temp variable
3. Make the node.next to new node
4. then new node.next to the temp variable

"""
from linked_list_basics import Node
from traversal import Traversal

class Insertion:

    @staticmethod
    def insert_at_begin(head_node: Node, val: int):
        new_node = Node(val)
        new_node.nxt = head_node 
        head_node = new_node 
        return head_node

    @staticmethod 
    def insert_at_end(head_node: Node, val: int):
        # edge case, linked list itself is empty
        if not head_node:
            return Node(val)
        curr = head_node 
        while curr.nxt: # go to the last node and not the pass the last node
            curr = curr.nxt
        curr.nxt = Node(val)
        return head_node
    
    @staticmethod 
    def insert_at_pos(head_node: Node, val: int, pos: int):
        # edge case, linked list itself is empty
        if not head_node:
            return Node(val)  
        curr = head_node
        for _ in range(pos-2):
            curr = curr.nxt 
        temp = curr.nxt 
        curr.nxt = Node(val)
        curr.nxt.nxt = temp 

        return head_node
            

if __name__ == "__main__":

    # Linked List Formation
    head = Node(5)
    node1 = Node(6)
    head.nxt = node1 
    node2 = Node(4)
    node1.nxt = node2 
    node3 = Node(8)
    node2.nxt = node3
    print("Before Updating..\n")
    tr = Traversal(head)
    tr.iterative_traversal()

    head = Insertion.insert_at_begin(head, 3)
    print("After Updating..\n")
    tr = Traversal(head)
    tr.iterative_traversal()

    head = Insertion.insert_at_end(head, 7)
    print("After Updating at end..\n")
    tr = Traversal(head)
    tr.iterative_traversal()

    pos = 2
    head = Insertion.insert_at_pos(head, 7, pos)
    print(f"After Updating at position {pos}..\n")
    tr = Traversal(head)
    tr.iterative_traversal()