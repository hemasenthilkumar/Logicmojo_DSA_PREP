

def searchPattern(txt, pat):
    # code here
    # TC = O(n*m)
    n = len(txt)
    m = len(pat)
    for i in range(n-m+1):
        j = 0
        while j<m and txt[i+j]==pat[j]:
            j += 1
        if j==m:
            return True
    return False