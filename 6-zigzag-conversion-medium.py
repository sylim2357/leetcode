# -----------------------------------------------------------
# Need Review
# Runtime: 64 ms, faster than 50.51% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.
# Comment: NA
# -----------------------------------------------------------

def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s
    rows = {idx: '' for idx in range(min(len(s), numRows))}
    i = 0
    direction = False
    for c in s:
        rows[i] += c
        if ((i==0) | (i==numRows-1)):
            direction = not direction
        if direction:
            i += 1
        else:
            i += -1
    answer = ''
    for idx in range(len(rows)):
        answer += rows[idx]
    return answer
