"""
Subarray with sum equal to X

Subarray - contigous sequence of elements
Subsequence - We can skip elements - order will be same though
Subset - We can skip elements, and no order needs to be maintained 

Version1: Non-negative number

(This approach will work for all positive elements only)
Approach 1: run for loop O(n^2)
Approach 2: Dynamic size Sliding window
"""

def subarray_target(arr, target):
    l = 0
    r = 0
    current_sum = 0
    n = len(arr)
    result = []
    while l <= r and r < n:
        # if multiple are required, then create a list and save it to the list
        if current_sum  == target:
            return arr[l:r]
            # for multiple save it to list and do 
            # l += 1s
        elif current_sum < target:
            # increase the window size
            current_sum += arr[r]
            r  += 1
        else:
            # reduce the sum 
            current_sum -= arr[l]
            l += 1

    return arr[l:r]

# negative number -> this approach wont work
# Hint
"""
Use a hashmap

X+[a+b+c+d] = target
  currSum
X = target-currSum
each time we will know the remaining sum we need

10 -> 2
12 -> 1
-10 -> 1
0 -> 1
"""

if __name__ == "__main__":
    print(subarray_target([2,4,6,1,8], 11))