"""
BIT MANIPULATION

BIT -> nibble -> byte

1 nibble = 4 BITs
1 byte   = 8 BITs

1. Bitwise AND
2. Bitwise OR
3. Bitwise XOR
4. Bitwise XOR
5. Left Shift (<<)
6. Right Shift (>>)
7. Complement (~)

1010
0110
--------
1110 (OR) = 2 + 4 + 8 = 14
1100 (XOR) = 4 + 8 = 12 

1100
0110
-----
0100 = 4
1110 = 14
1010 = 10

Left shift -> shift bits to the left
5 << 1

0000101
0001010 = 10

5 << 2
0000101
0010100 4 + 16 = 20

8 << 3
00001000
00010000
00100000 = 1,2,4,8,16,32,64

SIMPLY ITS BEING MULTIPLED BY 2**3 times.

Right Shift 

8 >> 1 

1000
0100 = 4

SIMPLY ITS BEING DIVIDED BY 2

60 >> 4 

0111100 = 4+8+16+32 = 60

0011110 = 2+4+8+16 = 30
0001111 = 1 + 2+ 4 + 8 = 15
0000111 = 1 + 2 + 4 = 7
0000011 = 3

Complement
----------------
0 -> 1
1 -> 0

Problems:
1. Get ith bit 
2. Set ith bit
3. Clear ith bit

N=10, i=2 

10 = 1010

Get 2nd bit = 0
Set ith bit = 1110 = 2 + 4 + 8 = 14
Clear ith bit = 1010 = 10

Trick
1. Get ith bit
N & (1 << i)

2. Set ith bit
N | (1 << i)

3. Clear ith bit
N | ~(1 << i)

14 =  1110
i = 3

1.Get ith bit

1110
1000 &
------
1000 = 1

2. Set ith bit

1110
1000 |
---------
1110

3. Clear ith bit

1110
0111 &
-------
0110


"""

def get_ith_bit(n: int, i: int) -> int:
    # TC, SC = O(1)
    mask = 1 << i 
    res = n & mask 
    return 0 if res == 0 else 1 

def set_ith_bit(n: int, i: int) -> int:
    # TC, SC = O(1)
    mask = 1 << i
    res = n | mask 
    return res

def clear_ith_bit(n: int, i: int) -> int:
    # TC, SC = O(1)
    mask = ~(1 << i)
    res = n & mask 
    return res

if __name__=="__main__":
    print(get_ith_bit(10,2))
    print(set_ith_bit(10,2))
    print(clear_ith_bit(10,2))



