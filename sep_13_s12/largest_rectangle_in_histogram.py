from typing import List
# O(n^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # check both left and right sides and calculate the max
        max_value = float('-inf')
        for i in range(len(heights)):
            currValue = heights[i]
            j = i - 1
            # check left side
            while j >=0 and heights[j] >= heights[i]:
                currValue += heights[i]
                j -= 1
            # check right side
            j = i+1
            while j < len(heights) and heights[j] >= heights[i]:
                currValue += heights[i]
                j += 1
            max_value = max(max_value, currValue)
        return max_value