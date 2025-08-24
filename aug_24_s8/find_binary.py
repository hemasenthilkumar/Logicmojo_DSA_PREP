"""
Find binary numbers with given number
"""

def find_binary_numbers(string, n):
    if len(string) == n:
        print(string)
        return 
    find_binary_numbers(string+'0', n)
    find_binary_numbers(string+'1', n)

if __name__ == "__main__":
    find_binary_numbers("", 3)