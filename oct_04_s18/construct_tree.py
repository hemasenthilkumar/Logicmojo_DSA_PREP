"""
Construct tree from traversals

To construct any BT, we can do from these options
- inorder + preorder
- inorder + postorder
- inorder + level order

"""


class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 


def construct(preorder, inorder, start, end, preindex):
    newnode = TreeNode(preorder[preindex])
    inindex = search_index()
    newnode.left = construct(preorder, inorder, start, )


def search_index():
    pass