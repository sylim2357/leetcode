# -----------------------------------------------------------
# First Attempt
# Runtime: 52 ms, faster than 86.95% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
# Comment: NA
# -----------------------------------------------------------

def isPalindrome(self, x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return 1
    else:
        return 0
