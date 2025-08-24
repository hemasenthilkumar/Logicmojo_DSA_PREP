"""
Towers of Hanoi

           Steps
Disc = 1 -> 1
Disc = 2 -> 3
Disc = 3 -> 7
Disc = 4 -> 15
Disc = 5 -> 31
Disc = 6 = 31 + 31 + 1 = 63

Formula = (n-1) Disc * 2  + 1

Goal: n Disc (A -> C) 
-------------------------------
n-1 Disc (A -> B) ---> this will be recursive
Pick and Place last (A-> C) --> direct command
n-1 (B->C) ---> this will be recursive
"""

# finding the count
# using formula
def towers_of_hanoi(n):
    if n == 1:
        return 1 
    return towers_of_hanoi(n-1)*2 + 1

# using algorithm and logic
def towers_of_hanoi_recur(n, source, dest, aux):
    """
    TC: O(2^n)
    SC: O(n)
    """
    if n==1:
        print(f"Moving disk {n} from source {source} to {dest}") # A to C
        return
    towers_of_hanoi_recur(n-1, source, aux, dest) # A to B
    print(f"Moving disk {n} from source {source} to {dest}")  # A to C
    towers_of_hanoi_recur(n-1, aux, dest, source) # B to C


if __name__ == "__main__":
    print(towers_of_hanoi(5))
    print(towers_of_hanoi_recur(3, 'A', 'C', 'B'))