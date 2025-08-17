"""
Two pointers with sum equal to X

Approach 1: Two For loops TC: O(n^2) SC: O(1)
Approach 2: Two pointers TC: O(nlogn) SC: O(1)
Approach 3: Mathematical approach with hashmap TC: O(n) SC: O(n)
"""
from collections import defaultdict

def two_sum(arr, target):
    arr.sort()
    l = 0
    r = len(arr) - 1
    res = []
    while l < r:
        if arr[l] + arr[r] == target:
            res.append([arr[l],arr[r]])
            l += 1 
        elif arr[l] + arr[r] < target:
            l += 1 
        else:
            r -= 1
    return res


def two_sum_a2(arr, target):
    cache = defaultdict(int)
    res = []
    for i in arr:
        if target - i in cache:
            res.append([i, target-i])
        else:
            cache[i] += 1
    return res

if __name__ == "__main__":
    print(two_sum([-2,-1,1,3,4,9], 7))
    print(two_sum_a2([-2,-1,1,3,4,9], 7))

