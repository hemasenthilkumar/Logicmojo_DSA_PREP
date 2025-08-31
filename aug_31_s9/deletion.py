
from linked_list_basics import Node
from traversal import Traversal

class Deletion:

    @staticmethod
    def delete(head_node: Node, key: int):

        # edge case -> head node we want to delete
        if head_node.data == key:
            return head_node.nxt 
        
        curr = head_node 

        while curr.nxt.data != key:
            curr = curr.nxt 

        to_delete = curr.nxt 
        to_join = to_delete.nxt 
        curr.nxt = to_join 

        return head_node
    
    @staticmethod
    def delete_a2(head_node: Node, key: int):

        if head and key == head_node.data:
            return head_node.nxt

        curr = head_node
        prev = None 

        while curr and curr.data != key:
            prev = curr 
            curr = curr.nxt
        if not curr:
            print("No matching key found!!")
            return None
        prev.nxt = curr.nxt  
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

    head = Deletion.delete_a2(head, 3)

    tf = Traversal(head)
    tf.iterative_traversal()