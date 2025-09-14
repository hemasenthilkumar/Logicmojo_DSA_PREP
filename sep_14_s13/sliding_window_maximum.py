from collections import deque
from typing import List

class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        # while removing from window then its left
        # while removing during condition then its right

        max_window = [0] * (len(nums) - k + 1)
        # eg. n = 8, k= 3, max_window = 8-3+1 = 6 ?
        # first process k elements
        i = 0
        j = 0
        while i < k:
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            i += 1
        max_window[j] = nums[dq[0]]
        j += 1
        # process remaining elements
        while i < len(nums):
            # remove all out of window numbers from left
            while dq and dq[0] <= i-k:
                dq.popleft()
            # remove smaller values from right
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # once done append it
            dq.append(i)
            i += 1
            # then later take the value
            max_window[j] = nums[dq[0]]
            j += 1
        return max_window

