"""
Binary to Decimal conversion O(number of bits)
"""

def binary_to_decimal(binary: str):
    total = 0
    for ind, i in enumerate(reversed(binary)):
        if int(i) == 1:
            total += 2**int(ind)
    return total

if __name__ == '__main__':
    print(binary_to_decimal('01010'))