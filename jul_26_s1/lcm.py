"""
LCM
Smallest number divisible by both a & b

Approach 1: Check if multiples of larger number are divisible by smaller number O(min(a,b))

Approach 2: Formula:  a*b/GCD(a,b)   O(1).O(log(min(a,b))) = O(log(min(a,b)))

"""
from gcd import find_gcd_a2_iter

def find_lcm_a1(smaller,bigger):
    
    lcm  = smaller * bigger
    for i in range(bigger, smaller*bigger+1, bigger):
        if i % smaller == 0:
            lcm = i
            break 
    return lcm

def find_lcm_a2(smaller, bigger):
    gcd_val = find_gcd_a2_iter(smaller, bigger)
    lcm = (smaller * bigger ) // gcd_val
    return lcm

if __name__ == "__main__":
    print(find_lcm_a1(12,18))
    print('*'*30)
    print(find_lcm_a2(12,18))