class Solution:
    """
    TC: O(N)
    SC: O(D) where D = depth
    """

    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1