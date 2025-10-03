from bfs import level_order

"""
TC: O(N)
SC: O(W) (max number of nodes at any level)
"""

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

# this is for binary tree
# this is similar to level order traversal
from collections import deque
def insert(root, data):
    newnode = TreeNode(data)
    if not root:
        return newnode
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        if not curr.left:
            curr.left = newnode
            break
        else:
            q.append(curr.left) 
        if not curr.right:
            curr.right = newnode 
            break 
        else:
            q.append(curr.right) 
    return root

if __name__ == "__main__":
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    root.left = node1 
    root.right = node2 
    node3 = TreeNode(31)
    node4 = TreeNode(61)
    node5 = TreeNode(51)
    node1.left = node3 
    node2.left = node4 
    node2.right = node5
    print("before inserting")
    print(level_order(root))
    for i in [11,2,4,5]:
        insert(root, i)
    print("after inserting")
    print(level_order(root))