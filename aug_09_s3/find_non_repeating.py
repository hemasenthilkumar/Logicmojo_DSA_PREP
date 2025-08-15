"""
Find two non repeating elements in an array of repeating elements

Eg:
Input: nums = [2, 4, 7, 9, 2, 4]
Output: [7, 9]
Explanation: 7 and 9 appear only once; all others appear twice.
"""


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
            i += 2
        else:
            res.append(x[i])
            i += 1 
    return res 

if __name__ == "__main__":
    x= [-1, -2, -1, -3, -2, -4]
    y =[10,20]
    z=[10]
    print(find_non_repeat(x))
    print(find_non_repeat_a2(x))
    print(find_non_repeat(y))
    print(find_non_repeat_a2(y))
    print(find_non_repeat(z))
    print(find_non_repeat_a2(z))