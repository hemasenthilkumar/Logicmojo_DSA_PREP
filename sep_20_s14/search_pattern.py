
def sliding_window(txt, pat):
    # O(m * n)
    i = 0
    matches = []
    j = 0
    for i in range(len(txt)-len(pat)+1):
        for j in range(len(pat)):
            if txt[i+j] != pat[j]:
                break
        else:
            matches.append(i)
    return matches


def searchPattern(txt, pat):
    # code here
    if len(pat) > len(txt):
        return False
    return bool(sliding_window(txt, pat))
    