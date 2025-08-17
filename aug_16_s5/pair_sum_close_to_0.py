


def two_sum_a1(arr):

    closestSum = float('inf')
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            currentSum = arr[i] + arr[j]
            if abs(currentSum) < abs(closestSum):
                closestSum = currentSum 
    return closestSum



def two_sum(arr):
    arr.sort()
    closestSum = float('inf')
    l=0
    r = len(arr) - 1
    res = []
    while l < r:
        currentSum = arr[l] + arr[r]
        if abs(currentSum) < abs(closestSum):
            closestSum = currentSum 
        if currentSum == 0:
            return 0
        if currentSum < 0:
            l += 1
        else:
            r -= 1
    return closestSum

if __name__ == "__main__":
   
   print(two_sum([-8, -2,2, -60]))
