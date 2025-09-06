class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        l = 0
        r = len(arr)-1
        result = set()
        
        while l < r:
            if arr[l] + arr[r] == 0:
                result.add((arr[l], arr[r]))
                l += 1
                r -= 1
            elif arr[l] + arr[r] > 0:
                r -= 1
            else:
                l += 1
        
        return sorted(list(result))