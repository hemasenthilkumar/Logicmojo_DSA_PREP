def theGreatXor(x):
    # Write your code here
    max_val = (1 << x.bit_length()) - 1
    return max_val - x