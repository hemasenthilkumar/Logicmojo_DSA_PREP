from collections import defaultdict
def maxLen(n, arr):
    # Write your code here
    """
    1. find prefix array and store it in cache dict
    2. if any value is 0, then store the length in max_len
    3. Then run through the cache dict and see the same occurrence of that value
    """
    prefix_dict = [0] * n
    prefix_dict[0] = arr[0]
    cache = defaultdict(list)
    cache[prefix_dict[0]].append(0)
    max_len = 0
    for i in range(1, len(arr)):
        prefix_dict[i] = prefix_dict[i-1] + arr[i]
        cache[prefix_dict[i]].append(i)
        if prefix_dict[i] == 0:
            max_len = max(max_len, i+1)
    for _, v in cache.items():
        if len(v) > 1:
            max_len = max(max_len, v[-1]-v[0])
    return max_len
            