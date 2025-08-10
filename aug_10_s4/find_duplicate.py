"""
Find duplicate number in array

1. Check each number and see if its present again in array O(N^2)
2. Take count hash map and pick the >1 item O(N) + Space O(N) 
3. XOR the full number array with given number o(N)
"""
from collections import defaultdict 

def find_duplicate_2(nums: int):
    freq = defaultdict(int)
    for i in nums:
        freq[i] += 1 
        if freq[i] > 1 :
            return i 

def find_duplicate_3(nums: int):
    full_nums = range(1,len(nums))
    y=full_nums[0]
    for i in full_nums[1:]:
        y = y ^ i
    x=nums[0]
    for i in nums[1:]:
        x = x ^ i
    return x ^ y

if __name__ == "__main__":
    print(find_duplicate_3([1,2,2,3,4,5]))
    print(find_duplicate_3([1,2,3,3,4,5,6]))