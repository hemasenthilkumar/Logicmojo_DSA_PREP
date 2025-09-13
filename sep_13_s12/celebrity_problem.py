def find_celebrity(matrix):
    n = len(matrix)
    
    stack = []
    for i in range(n):
        stack.append(i)
    # eliminate till there is more than 1 person
    # checking the possibility
    while len(stack) > 1:
        first = stack.pop()
        second = stack.pop()

        if matrix[first][second] == 1:
            stack.append(second)
        else:
            stack.append(first)
        
        # both knows each other or doesnt know each 
    if not stack:
        return -1 
    
    celeb = stack.pop()

    # celeb should not know anyone 
    for i in range(n):
        if celeb !=i and matrix[celeb][i] == 1:
            return -1 
    # everyone should know celeb  

    for i in range(n):
        if matrix[i][celeb] == 0:
            return -1 
    return celeb  

if __name__ == "__main__":
    x = find_celebrity([100,80,60,70,60,75,86])
    print(x)