"""
Just backtracking solution
"""

class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        return self.recurse(arr, 0, sum)
        
    
    def recurse(self, arr, index, target):
        if target == 0:
            return True   
        # base condition
        if index >= len(arr):
            return False

        
        # pick
        pick_val = self.recurse(arr, index+1, target-arr[index])
        npick_val = self.recurse(arr, index+1, target)
        
        return pick_val or npick_val
        
        