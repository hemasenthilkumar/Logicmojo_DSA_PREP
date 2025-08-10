"""
Find Odd Occurence elements O(N)
"""

def find_odd_occur(nums: list) -> int:
    xor = nums[0]
    for num in nums[1:]:
        xor = xor ^ num 
    return xor 

if __name__ == "__main__":
    print(find_odd_occur([2,7,7,7,2]))