
from collections import deque
from bfs import level_order

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def insert_bst(curr, data):
    if curr is None:
        return TreeNode(data)
    if data < curr.data:
        curr.left = insert_bst(curr.left, data) 
    else:
        curr.right = insert_bst(curr.right, data)
    return curr

if __name__ == "__main__":
    root = None
    for i in [4,2,7,1,3, 5]:
        root = insert_bst(root, i)
    print(level_order(root))