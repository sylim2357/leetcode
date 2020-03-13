# -----------------------------------------------------------
# Failure. Need Review
# Runtime: 64 ms, faster than 60.50% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Comment: NA
# -----------------------------------------------------------

def lengthOfLongestSubstring(self, s: str) -> int:
    substr = {}
    ans = 0
    i = 0
    for j in range(len(s)):
        if s[j] in substr.keys():
            i = max(substr[s[j]]+1, i)
        ans = max(ans, j-i+1)
        substr[s[j]] = j
    return ans
