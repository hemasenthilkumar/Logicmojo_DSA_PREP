
from linked_list_basics import Node

class Traversal:

    def __init__(self, head_node: Node):
        self.head = head_node 

    def iterative_traversal(self):

        curr = self.head 
        while curr:
            print(f"{curr.data}-->", end="")
            curr = curr.nxt 
        print("NULL")
    
    def recursive_traversal(self, current_node):

        if current_node == None:
            return 
        print(current_node.data)
        self.recursive_traversal(current_node.nxt)



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
    print("\n")
    tr.recursive_traversal(head)