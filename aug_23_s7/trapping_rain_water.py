"""
Building left & right max array approach

TC: O(N)
SC: O(N)

Two Pointer Approach

TC: O(N)
SC: O(1)
"""

def max_water(arr):
    
    n = len(arr)

    left_max = [0] * n
    right_max = [0] * n
    # precompute left max
    for i in range(1,len(arr)):
        left_max[i] = max(left_max[i-1], arr[i-1])

    # precompute right max
    right_max[-1] = 0
    for i in range(len(arr)-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i+1])
    
    # find save water for each block
    save = 0
    for i in range(1, len(arr)):
        # formula 
        save += max(0,min(left_max[i], right_max[i])-arr[i])

    return save

# optimizing space complexity
"""
lMax = 0
rMax = 0
"""

def two_pointer_approach(arr):
    n = len(arr)
    l = 0
    r = n - 1 
    leftMax = 0
    rightMax = 0
    totalWater = 0

    while l < r:
        # if left height is smaller than right, then 
        # we cant do anything much
        if arr[l] < arr[r]:
            if arr[l] >= leftMax:
                leftMax = arr[l]
            else:
                totalWater += leftMax-arr[l]
            l += 1
        else:
            if arr[r] >= rightMax:
                rightMax = arr[r]
            else:
                totalWater += rightMax - arr[r]
            r -= 1 
    return totalWater


if __name__ == "__main__":
    print(max_water([0,1,0,2,1,0,1,3,4,1,2,1]))
    print(two_pointer_approach([0,1,0,2,1,0,1,3,4,1,2,1]))