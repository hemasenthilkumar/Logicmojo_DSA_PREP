"""
Find two non repeating elements in an array of repeating elements

Eg:
Input: nums = [2, 4, 7, 9, 2, 4]
Output: [7, 9]
Explanation: 7 and 9 appear only once; all others appear twice.
"""

def find_non_repeat(x):
    # TC: O(nlogn)
    # Sort: O(nlogn) + Traverse: O(n) 
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
    print(find_non_repeat(x))