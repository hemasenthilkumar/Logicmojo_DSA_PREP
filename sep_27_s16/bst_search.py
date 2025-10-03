
from collections import deque
from bfs import level_order
from bst_insertion import insert_bst

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def search_bst(curr, data):
    if curr is None:
        return None
    if curr.data == data:
        return curr
    if data < curr.data:
        return search_bst(curr.left, data) 
    else:
        return search_bst(curr.right, data)

if __name__ == "__main__":
    root = None
    for i in [4,2,7,1,3, 5]:
        root = insert_bst(root, i)
    print(level_order(root))
    root2 = search_bst(root, 2)
    print(level_order(root2))