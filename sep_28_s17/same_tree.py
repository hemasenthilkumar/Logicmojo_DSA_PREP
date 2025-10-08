"""
TC: O(Min(N, M))
SC: O(H) where H = min height of both trees

"""

class Solution:
    def isSameTree(self, p,  q) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        p_left = p.left if p.left else None
        q_left = q.left if q.left else None
        p_right = p.right if p.right else None
        q_right = q.right if q.right else None
        return p.val == q.val and self.isSameTree(p_left, q_left) and self.isSameTree(p_right, q_right)