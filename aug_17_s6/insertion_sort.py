"""
Insertion Sort

TC: O(n^2)
SC: O(1)
Best case TC: O(n)
"""

def insertion_sort(arr):
    for i in range(len(arr)):
        value = arr[i] 
        hole = i -1 

        while (hole >= 0 and arr[hole] >= value) :
            arr[hole+1] = arr[hole] # for shifting to right
            hole -= 1 
        

        arr[hole+1] = value 
    
    return arr 

if __name__ == "__main__":
    print(insertion_sort([25, 37, 10, 11, 11, 34]))