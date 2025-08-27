def findPeakElement(nums) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + ((r-l)//2)
            left = nums[mid-1] if mid-1 >= 0  else float('-inf')
            right = nums[mid+1] if mid+1 < len(nums) else float('-inf')
            if left < nums[mid] > right:
                return mid
            elif left > right:
                r = mid -1 
            else:
                l = mid + 1
        