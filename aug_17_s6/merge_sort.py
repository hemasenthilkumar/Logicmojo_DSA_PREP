"""
Merge Sort
"""

def merge(arr, l, mid, r):
    n1 = mid-l+1 # first half size
    n2 = r - mid # second half size
    left = [0] * n1 
    right = [0] * n2 
    for i in range(n1):
        # create temp array 
        """

        7 2 5 4 3
        l = 0
        r = 4
        mid = 2 

        left split:  7 2 5 (l=0  r=2)
        right split:  4 3 (l=3 r=4)
        
        """
        left[i] = arr[i+l]

    for i in range(n2):
        # create temp array 
        right[i] = arr[i+mid+1]


    i, j = 0,0
    k = l # l will be the starting value instead of always 0
    while i < n1  and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    # dump all remaining elemts
    while i < n1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < n2:
        arr[k] = right[j]
        k += 1
        j += 1


def split_and_merge(arr, l, r):
    if l < r:
        mid = l + ((r-l)//2)
        split_and_merge(arr, l, mid)
        split_and_merge(arr, mid+1, r)
        merge(arr, l, mid, r)

def mergeSort(arr):
    split_and_merge(arr, 0, len(arr)-1)

if __name__ == "__main__":
    arr = [7,2,1,5,3,8,2,0]
    mergeSort(arr)
    print(arr)