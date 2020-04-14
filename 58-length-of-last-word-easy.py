# -----------------------------------------------------------
# Second Attempt
# Runtime: 20 ms, faster than 95.98% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Length of Last Word.
# Comment: NA
# -----------------------------------------------------------

def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == ' ':
            return len(s) - i -1
    return len(s)
