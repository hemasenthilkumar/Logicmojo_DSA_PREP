def maximumDifference(nums):
        solution = -1
        minVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > minVal:
                solution = max(solution, nums[i]-minVal)
            else:
                minVal = nums[i]
        return solution

