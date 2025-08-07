"""
GCD of 2 numbers
smallest number which can divide both a & b

Approach 1: reduce the smaller number untill it divides both smaller & bigger number O(min(a,b))

Approach 2: Euclidean Algorithm  O(log(min(a,b)))
"""

def find_gcd_a1(smaller, bigger):
    gcd = 0
    for i in range(smaller, 0, -1):
        if smaller%i==0 and bigger%i == 0:
            gcd = i 
            break 
    return gcd

def find_gcd_a2_recur(smaller, bigger):
    """
    GCD(A,0) = A
    GCD(0,B) = B 
    A = B.Q + R
    GCD(A,B) == GCD(B,R)

    Eg.
    GCD(54, 28) = 54 = 28 * 1 + 26 
    GCD(28, 26) = 28 = 26*1 + 2 
    GCD(26, 2) = 26 = 2*13 + 0
    GCD(2,0) = 2
    """
    if smaller == 0:
        return bigger
    return find_gcd_a2_recur(bigger%smaller, smaller)

def find_gcd_a2_iter(smaller, bigger):
    while smaller > 0:
        bigger, smaller = smaller,  bigger % smaller 
    return bigger


if __name__ == "__main__":
    print(find_gcd_a1(28, 54))
    print(find_gcd_a1(36, 60))
    print(find_gcd_a1(5, 17))
    print("*"*30)
    print(find_gcd_a2_recur(28, 54))
    print(find_gcd_a2_recur(36, 60))
    print(find_gcd_a2_recur(5, 17))
    print("*"*30)
    print(find_gcd_a2_iter(28, 54))
    print(find_gcd_a2_iter(36, 60))
    print(find_gcd_a2_iter(5, 17))