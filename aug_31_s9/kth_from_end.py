from linked_list_basics import Node

def kth_node_from_end(head_node: Node, k: int):
    # using slow and fast pointers
    slow = head_node
    fast = head_node
    for _ in range(k):
        if fast:
            fast = fast.nxt 
    
    while fast:
        slow = slow.nxt 
        fast = fast.nxt 
    
    return slow.data

if __name__ == "__main__":

    # Linked List Formation
    head = Node(5)
    node1 = Node(6)
    head.nxt = node1 
    node2 = Node(4)
    node1.nxt = node2 
    node3 = Node(8)
    node2.nxt = node3
    node4 = Node(7)
    node3.nxt = node4
    
    print(kth_node_from_end(head, 2))