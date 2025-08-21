def maximizingXor(l, r):
    # Write your code here
    max_res = float('-inf')
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            if i ^ j > max_res:
                max_res = i ^ j
    return max_res