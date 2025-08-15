"""
Given an array where every element appears three times except one, find that one element

Input: nums = [2, 2, 3, 2]
Output: 3
Explanation: 3 appears once, while every other element appears exactly three times.
"""

# PENDING: Need to think for solution O(N) or O(1) with space also O(1) may be using bit manipulation

def find_non_repeat_a2(x):
    # TC: O(n)
    # SC: O(n)
    freq_dict = {}
    for i in x: # O(n)
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1 
    res = []
    for k,v in freq_dict.items():  # O(n)
        if v == 1:
            res.append(k)
    return res

def find_non_repeat(x):
    # TC: O(nlogn)
    # Sort: O(nlogn) + Traverse: O(n) 
    # SC: O(1)
    res = []
    i = 0
    x.sort()
    while i < len(x):
        print(x[i])
        if i+1 < len(x) and x[i] == x[i+1]:
            i += 3
        else:
            res.append(x[i])
            i += 1 
    return res 

if __name__ == "__main__":
    x= [2, 2, 3, 2]
    y =[0, 1, 0, 1, 0, 1, 99]
    z=[10]
    print(find_non_repeat(x))
    print(find_non_repeat_a2(x))
    print(find_non_repeat(y))
    print(find_non_repeat_a2(y))
    print(find_non_repeat(z))
    print(find_non_repeat_a2(z))