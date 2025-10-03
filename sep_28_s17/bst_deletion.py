"""
If the node is a leaf -> simply delete
If one child -> update the node with the child & delete
If 2 children -> you can plan to go with either of them
- but if a node already has 2 children, then its difficult
- so we have to take the next bigger number as per the inorder traversal
- to find the next number , go to the right, and keep on going left to find it
"""


from collections import deque
from sep_27_s16.bfs import level_order


class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def delete_from_bst(curr, data):
    if not curr:
        return curr 
    if data < curr.data:
        curr.left =  delete_from_bst(curr.left, data)
    elif data > curr.data:
        curr.right = delete_from_bst(curr.right, data)
    else:
        # if leaf 
        if curr.left is None and curr.right is None:
            return None 
        # Single child
        if curr.left is None and curr.right:
            return curr.right
        if curr.right is None and curr.left:
            return curr.left
        # Two Children
        # replace with next bigger traversal
        nextb = curr.right 
        while nextb and nextb.left:
            nextb = nextb.left
        curr.data = nextb.data
        return curr 
    return curr
    