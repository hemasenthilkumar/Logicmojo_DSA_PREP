"""
Selection Sort

TC: O(n^2)
"""

def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j 
        # now since we found the min value index 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr 

if __name__ == "__main__":
    print(selection_sort([25, 37, 10, 11, 11, 34]))