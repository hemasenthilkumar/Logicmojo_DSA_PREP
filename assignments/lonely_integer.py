def lonelyinteger(a):
    # Write your code here
    y = a[0]
    for i in a[1:]:
        y = y ^ i
    return y