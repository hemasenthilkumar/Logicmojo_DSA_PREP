"""
You are given an integer n and an integer array arr of size n+2. 
All elements of the array are in the range from 1 to n.
Also, all elements occur once except two numbers which occur twice. 
Find the two repeating numbers.

Approach 1: Check all elements O(n^2)
Approach 2: Sort and compare a[i] == a[i+1] O(nlogn)
Approach 3: Frequency map O(n), SC= O(n)
Approach 4: Summation O(n) , SC=O(1)
Approach 5: Indexing O(n)(Since its ranging from 1 to N, we can track the index according to that)
Approach 6: XOR
    1. Arr ^ [1 to N]
    2. Take the bits from the result
    3. Divide the Arr, [1 to N] in the set bits bucket
    4. Do a xor of those buckets individually
"""

def get_2_repeated(arr):
    res = []
    for a in arr:
        index = abs(a)
        if arr[index]  > 0:
            arr[index] = arr[index] * -1 
        else:
            # the index (array value which is considered as index) has been repeated
            res.append(index)
    
    return res 

def get_2_repeated_xor(arr, n):
    """
    1. Take XOR of array with (1..n)
    2. Here we get XOR = c (a^b)
    3. Now to seperate c into a and b, we will split c into 2 bucket and reduce the problem to single duplicate
    4. To separate, add check on rightmost set bit 
    """
    # take xor of array
    xor = 0
    for num in arr:
        xor = xor ^ num
    for i in range(1, n+1):
        print(i)
        xor = xor ^ i 

    num1 = 0
    num2 = 0

    # split logic
    # 1. split input  array
    for num in arr:
        if xor & num == 0:
            print(xor, num)
            num1 ^= num 
        else:
            num2 ^= num 
    # 2. split range array 
    for num in range(1, n+1):
        if xor & num == 0:
            num1 ^= num 
        else:
            num2 ^= num
    print(num1, num2)     

if __name__ == "__main__":
    x = [1,2,1,3,4,3]
    #print(get_2_repeated(x))
    get_2_repeated_xor(x, 4)