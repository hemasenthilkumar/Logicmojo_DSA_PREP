"""
Can move up, down, left, right
end goal - able to reach (n-1, n-1)
starting position = 0,0

Up = diff row, same column (-1, 0)
Down = diff row, same column (1, 0)
left = same row, col decrease (0,-1)
right = same row, col increase (0, 1)

TC: 4^n^2
SC: n^2

Safe method:
- boundary
- cell value is 1
- tracking visited matrix
"""