"""
1. Majority Element - the element appears more than n/2 times in an array

Eg. 
arr = [8,5,8,2,5,5,5,5]
n = 8
n/2 = 4
Majority element  = 5

arr=[3,2,3,2]
n = 4
n = 2
No majority element

Approach 1: Using frequency map TC: O(n) SC: O(n)
Approach 2: Moore Voting Algorithm
   - support at most 1 candidate
   - If person votes for one of them -> increase
   - If someone new comes and place is vacant -> give a slot
   - If slot is occupied, reduce vote count for both

Eg. [8, 5,8,2,5,5,5,5]

"""

def get_majority(arr):
    candidate = 0
    votes = 0
    for i in arr:
        if votes == 0:
            candidate = i 
            votes += 1
        else:
            if i == candidate:
                votes += 1 
            else:
                votes -= 1
    votes = 0
    for i in arr:
        if i == candidate:
            votes += 1
    if votes > len(arr)/2:
        return candidate
    return -1

if __name__ == "__main__":
     print(get_majority([8,5,8,2,5,5,5, 9]))