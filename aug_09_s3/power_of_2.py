"""
Power of 2

If u do N-1 from N then all bits towards the right side will be flipped
along the right most set bit

all will be flipped from left most set bit
2(10) -> 1(01)
4(100) -> 3(011)
8(1000) -> 7(011)

for non powers of 2, right most bit and remaining will be flipped
6(110) -> 5(101)


only right most bit is flipped
3(11) -> 2(10)
5(101) -> 4(100)
13(1101) -> 12(1100)

For power of bit, only 1 bit will be set
Solution:

N & (N-1)
coz N-1 will be a complement of N 
then if result = 0 --> then its power of 2
"""

def is_power_of_2(n: int):
    # TC, SC = 0
    if n == 0:
        return False
    return n & (n-1) == 0

if __name__ == "__main__":
    print(is_power_of_2(64))
    print(is_power_of_2(3))
    print(is_power_of_2(0))