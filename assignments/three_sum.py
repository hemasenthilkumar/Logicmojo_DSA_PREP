"""
Three Sum

Brute Force Approach: O(n^3)
Approach 2: Two Sum TC: O(n^2) SC: O(N)
Approach 3: Two Sum TC: O(n^2logn) SC: O(1)
"""

# approach 2
class Solution:
    def twoSum(self, arr, target):
        cache = {}
        for n in arr:
            if target-n  in cache:
                return True
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
        return False
            
        
    def hasTripletSum(self, arr, target):
        # Code Here
        res = False
        for i,num in enumerate(arr):
            new_arr = list(arr)  # or list(arr) then pop(i)
            del new_arr[i]
            res = self.twoSum(new_arr, target-num)
            if res:
                return True
        return False
    
# Approach 3
def two_sum_a3(arr, target, start):
    l = start
    r = len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target:
            return True 
        if arr[l] + arr[r] < target:
            l += 1 
        else:
            r -= 1
    return False 

def three_sum_a3(arr, target):
    
    arr.sort()
    for i in range(len(arr)-2):
        res = two_sum_a3(arr, target-arr[i], i + 1)
        if res:
            return True 
    return False


## returning non duplicate pairs

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res = self.twoSum(nums, nums[i], i + 1)
            if res:
                result = result + res

        return result

    def twoSum(self, arr, pivot, start):
        l = start
        r = len(arr) - 1
        res = []
        while l < r:
            total = pivot + arr[l] + arr[r]
            if total == 0:
                res.append( [pivot, arr[l], arr[r]])
                # skip duplicates logic
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while r > l and arr[r] == arr[r-1]:
                    r -= 1
                
                # move to new elements
                l += 1
                r -= 1
            elif total < 0:
                l += 1 
            else:
                r -= 1
        return res
    