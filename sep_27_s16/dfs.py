"""
TC: O(N)
SC: O(H) - Height 
"""

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def preorder(root: TreeNode, res: list):
    if not root:
        return  
    res.append(root.data)
    preorder(root.left, res)
    preorder(root.right, res)

def inorder(root: TreeNode, res: list):
    if not root:
        return  
    inorder(root.left, res)
    res.append(root.data)
    inorder(root.right, res)

def postorder(root: TreeNode, res: list):
    if not root:
        return  
    postorder(root.left, res)
    postorder(root.right, res)
    res.append(root.data)

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

    res = []
    preorder(root, res)
    print(res)

    res = []
    inorder(root, res)
    print(res)

    res = []
    postorder(root, res)
    print(res)