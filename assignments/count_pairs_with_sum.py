class Solution:
    def countPairs(self, arr, target):
        #code here
        cache = {}
        count = 0
        for n in arr:
            diff = target -n 
            if diff in cache:
                count += cache[diff]
            cache[n] = cache.get(n,0) + 1
        return count