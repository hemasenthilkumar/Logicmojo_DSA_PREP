# O(N) using monotonic stack

class Solution:
    from typing import List
    def largestRectangleArea(self, heights: List[int]) -> int:
        # next smaller - right arr
        # prev smaller - left arr
        left_arr = [0] * len(heights)
        right_arr = [0] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                right_arr[stack.pop()] = i
            stack.append(i)
        while stack:
            right_arr[stack.pop()] = len(heights)
        
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                left_arr[stack.pop()] = i
            stack.append(i)
        while stack:
            left_arr[stack.pop()] = -1
    
        max_value = float('-inf')
        for i in range(len(heights)):
            val = ((right_arr[i] - left_arr[i]) - 1) * heights[i]
            max_value = max(max_value, val)
        
        return max_value