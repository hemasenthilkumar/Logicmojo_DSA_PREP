# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass

# TC: O(N)
# SC: O(1)

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = -1
        i = 0
        j = n-1
        while i < j:
            if knows(i, j):
                i += 1
            else:
                j -= 1
        
        celeb = i
        for col in range(n):
            if col != celeb and knows(celeb, col):
                return -1 
        for row in range(n):
            if row != celeb and knows(row, celeb) is False:
                return -1 

        return celeb 
