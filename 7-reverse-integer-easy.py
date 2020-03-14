# -----------------------------------------------------------
# Second Attempt. First was unnecessarily complicated
# Runtime: 32 ms, faster than 49.13% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
# Comment: NA
# -----------------------------------------------------------

def reverse(x: int) -> int:
    num = str(x)
    neg = False
    if x < 0:
        neg = True
        num = num[1:]
    num = num[::-1]
    if neg:
        num = '-' + num
    num = int(num)
    if (num > 2**31-1) or (num < -2**31):
        return 0
    else:
        return int(num)
