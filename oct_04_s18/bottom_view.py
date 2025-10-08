from collections import defaultdict
class Solution:
    def bottomView(self, root):
        # code here
        tree_map = defaultdict(lambda: defaultdict(list))

        def helper(curr, row, col, tree_map):
            if not curr:
                return None
            tree_map[col][row].append(curr.data)

            helper(curr.left, row+1, col-1, tree_map)
            helper(curr.right, row+1, col+1, tree_map)
        
        helper(root, 0,0, tree_map)
        result = []
        for cols in sorted(tree_map.keys()):
            temp = []
            for row in sorted(tree_map[cols].keys()):
                temp.extend(sorted(tree_map[cols][row]))
        
            result.append(temp)
        
        bottom_view = []
        for items in result:
            bottom_view.append(items[-1])
        return bottom_view
    