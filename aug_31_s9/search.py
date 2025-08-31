from linked_list_basics import Node
from traversal import Traversal

class Search:

    @staticmethod 
    def search(head_node: Node, key: int):

        curr = head_node 
        while curr:
            if curr.data == key:
                return curr 
            curr = curr.nxt 
        
        return None # if not found, it will return None
        

if __name__ == "__main__":

    # Linked List Formation
    head = Node(5)
    node1 = Node(6)
    head.nxt = node1 
    node2 = Node(4)
    node1.nxt = node2 
    node3 = Node(8)
    node2.nxt = node3

    print(Search.search(head, 3))
    print(Search.search(head, 8))