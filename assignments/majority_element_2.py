from collections import defaultdict

def majorityElement(nums):
        cache = defaultdict(int)
        # boyer moore algorithm
        for i in range(len(nums)):
            cache[nums[i]] += 1
            if len(cache) <= 2:
                continue
            # decrement 1
            # 0 remove
            new_cache= defaultdict(int)
            for k,v in cache.items():
                if v > 1:
                    new_cache[k] = v - 1
            cache = new_cache
        res = []
        for k,v in cache.items():
            if nums.count(k) > (len(nums)//3):
                res.append(k)
        return res 
        