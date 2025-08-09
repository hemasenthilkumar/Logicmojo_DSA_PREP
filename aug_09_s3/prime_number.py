"""
Prime number using Sieve of eratosthenes

TC = N * Harmony Progression of Prime numbers = N * log(log N)
SC = O(N)

"""
import math

def find_all_prime(n: int) -> list: 
    result = [True] * (n+1)  # all numbers are considered prime at first
    #result = {}
    # all factors should be there from 2 to root(n)
    #for i in range(2, n+1):
    #    result[i] = True 
    for i in range(2, int(math.sqrt(n))+1):
        # iterate inner loop for prime numbers only
        if result[i]:
            # mark all the factors are non prime
            for j in range(i*i, n+1, i):  # this will run n/i where i is the prime
                # so it will be n/2 + n/3 + n/5 ...N
                # so it will be n * (1/2 + 1/3 + 1/5 + 1/7 ...)
                # which is N * HP of prime numbers
                result[j] = False 
    return result 

if __name__=="__main__":
    x=find_all_prime(20)
    for i in range(2,len(x)):
        if x[i]:
            print(i)