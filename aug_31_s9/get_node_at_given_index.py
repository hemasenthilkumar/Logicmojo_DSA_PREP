
from linked_list_basics import Node
from traversal import Traversal

def get_node_at_given_index(head_node: Node, index: int):
    
    curr = head_node 
    counter  = 0
    while curr: 
        if counter == index-1:
            return curr 
        curr = curr.nxt 
        counter += 1
    return None


if __name__ == "__main__":

    # Linked List Formation
    head = Node(5)
    node1 = Node(6)
    head.nxt = node1 
    node2 = Node(4)
    node1.nxt = node2 
    node3 = Node(8)
    node2.nxt = node3
    
    print(get_node_at_given_index(head, 3).data)