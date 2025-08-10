"""
Recursion: When a function calls itself

1. base condition
2. Recursive stack -> space complexity
"""

def find_factorial(n: int):
    if n == 1:
        return 1 
    return n * find_factorial(n-1)

if __name__=="__main__":
    print(find_factorial(5))
    