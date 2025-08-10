"""
2 Types of search in Linear data structure

1. Linear Search / Sequential Search
2. Interval based search - Binary search
    Will work in sorted arrays
    Will divide the array in half size
"""

def binary_search_iter(arr: list, target: int) -> int:
    left, right = 0, len(arr)-1
    while left < right:
        mid = left + ((right-left)//2)
        if arr[mid] == target:
            return mid 
        elif target < arr[mid]:
            right = mid - 1 
        else:
            left = mid + 1
    return -1 

def binary_search_recur(arr: list, target: int, left: int, right: int) -> int:
    if left >= right:
        return -1 
    mid = left + ((right - left)//2)
    if arr[mid] == target:
        return mid 
    if target < arr[mid]:
        return binary_search_recur(arr, target, left, mid-1)        
    return binary_search_recur(arr, target, mid+1, right)  

if __name__=="__main__":
    arr = [1,2,3,4,5]
    x = 8
    print(binary_search_iter(arr, x))
    print(binary_search_recur(arr, x, 0, len(arr)-1))