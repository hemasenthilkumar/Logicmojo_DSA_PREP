"""
Bubble Sorting

TC: O(n^2)
"""

def bubble_sort(arr):

    for i in range(0, len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr 

if __name__ == "__main__":
    print(bubble_sort([5,2,1,9,4,3]) )   
