"""

"""

def segregate_01(arr):
    l = 0
    r = len(arr)-1

    while l < r:
        while l < r and arr[l] == 0:
            l += 1
        while l< r and arr[r] == 1:
            r -= 1
        if l< r:
            arr[l], arr[r] = arr[r], arr[l]

    return arr 

if __name__ == "__main__":
    print(segregate_01([0,1,1,0,1,0,1,0]))