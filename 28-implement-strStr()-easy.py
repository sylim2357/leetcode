# -----------------------------------------------------------
# Failure. Need Review
# Runtime: 20 ms, faster than 97.95% of Python3 online submissions for Implement strStr().
# Memory Usage: 13.1 MB, less than 92.31% of Python3 online submissions for Implement strStr().
# Comment: NA
# -----------------------------------------------------------

def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    needle_length = len(needle)
    for i in range(len(haystack)-needle_length+1):
        if haystack[i:i+needle_length] == needle:
            return i
    return -1
