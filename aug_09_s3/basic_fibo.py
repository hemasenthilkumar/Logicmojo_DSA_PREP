"""
Basic Iterative Fibonacci

TC: O(N)
SC: O(1)
"""

def fibo_series(n: int):
    a= 0
    b = 1
    print(a, end=" ")
    print(b, end= " ")
    for i in range(2, n+1):
        c = a + b 
        a = b 
        b = c 
        print(c, end = " ")

if __name__=="__main__":
    fibo_series(10)
