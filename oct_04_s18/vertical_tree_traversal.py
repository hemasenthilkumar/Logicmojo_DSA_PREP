"""
Vertical Tree Traversal
- its kind of opposite of level order traversal
"""
from collections import defaultdict
from typing import List

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

class Solution:
    def verticalTraversal(self, root) -> List[List[int]]:
           # its a map of map of list
            tree_map = defaultdict(lambda: defaultdict(list))

            def helper(curr, row, col, tree_map):
                if not curr:
                    return None
                tree_map[col][row].append(curr.val)

                helper(curr.left, row+1, col-1, tree_map)
                helper(curr.right, row+1, col+1, tree_map)
            
            helper(root, 0,0, tree_map)
            print(tree_map)
            result = []
            for cols in sorted(tree_map.keys()):
                temp = []
                for row in sorted(tree_map[cols].keys()):
                    temp.extend(sorted(tree_map[cols][row]))
            
                result.append(temp)
            return result