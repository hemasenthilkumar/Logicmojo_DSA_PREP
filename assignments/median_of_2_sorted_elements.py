class Solution:
    from typing import List
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # intuition => find the left partition array

        A = nums1
        B = nums2
        # prefer A is smaller one
        if len(B) < len(A):
            A,B = B, A

        l = 0
        r = len(A)-1
        total = len(A) + len(B)
        half = total//2
        # we will always find the median
        while True:
            i = l + ((r-l)//2) # mid point of A
            j = half - (i+1) - 1 # mid point of B

            ALeft = A[i] if i >=0 else float('-inf')
            ARight = A[i+1] if i+1 < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j+1] if j+1 < len(B) else float('inf')

            # check if we have found the correct partition
            if ALeft <= BRight and BLeft <= ARight:
                # find the median
                # odd
                if total %2  == 1:
                    return min(ARight, BRight)
                # even 
                return (max(ALeft, BLeft) + min(ARight, BRight))/2
            # wrong partition
            else:
                # we have more elements on A
                if ALeft > BRight:
                    r = i - 1
                else:
                    l = i + 1
                    
                 