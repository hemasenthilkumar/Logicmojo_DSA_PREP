def sort_an_array(n, arr):
    # Write your code here
    i = 0
    j = len(arr) - 1
    k = 0
    
    while k <= j:
        if arr[k] == 0:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
            i += 1
        elif arr[k] == 1:
            k += 1
        else:
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
    return arr