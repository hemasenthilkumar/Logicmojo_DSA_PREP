"""
TC: O(N)
SC: O(N)
"""

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

from collections import deque
def level_order(root: TreeNode):
    # FIFO property
    res=[]
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        res.append(node.data)

    return res


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

    print(level_order(root))