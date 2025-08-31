"""
Linked List
- Linear data structure
- Non-contiguous memory allocation

Important Topics
- Insertion
- Traversal
- Reverse
- Deletion
- Search


class Node:
    int data
    Node *net

"""

class Node:

    def __init__(self, data):
        self.data = data 
        self.nxt = None

