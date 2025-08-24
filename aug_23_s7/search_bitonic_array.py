"""
Find bitonic point
- stricttly increasing and then strictly decreasing (Bitonic Sequence)
- we have to find the max point

Linear Search Approach:

max point -> greater than left side and greater than right side
a[index-1] < a[index] > a[index+1]

We can iterate to get this condition to be true

TC: O(n)
SC: O(1)

Another Approach:
Left side is sorted
Right side is sorted
but we dont know the point -> we can use binary search

7 6 5 4
Terminating condition: a[mid] > a[mid-1] && a[mid] > a[mid+1]
elif Mid lies on left: a[mid] < a[mid +1] and a[mid] > a[mid-1] --> then l = mid + 1
elif Mid lies on right: a[mid] < a[mid-1] and a[mid] > a[mid+1] --> then r = mid - 1

"""

def get_bitonic_point(arr):
    # it will return the point instead of the element
    l = 0
    r = len(arr) - 1 

    while l <= r:
        mid = l + ((r-l)//2)
        if mid > 0 and mid < len(arr)-1 and arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return mid
        elif mid < len(arr)-1 and arr[mid] < arr[mid+1]:
            l = mid + 1 # mid lies left
        else:
            r = mid - 1 
            # sometimes r = mid
    return mid

if __name__ == "__main__":
    print(get_bitonic_point([1,2,6,7,8,7,4,3,1]))
    print(get_bitonic_point([1,2,6,7,8]))
    print(get_bitonic_point([5,4,3,2,1]))