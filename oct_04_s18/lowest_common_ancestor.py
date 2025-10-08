"""
LCA
- worst case - root node

A1 Flow
- get the path to the node from root
- get the last common node (traverse from last)

A2 Flow
if both right, and left are null or not null - return the val to the parent
once all are returned to the root , that will be the value

"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        if root == p or root == q:
            return root
        leftlca = self.lowestCommonAncestor(root.left, p, q)
        rightlca = self.lowestCommonAncestor(root.right, p, q)

        if leftlca and rightlca:
            return root
        return rightlca if rightlca else leftlca