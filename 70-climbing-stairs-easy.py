# -----------------------------------------------------------
# First Attempt
# Runtime: 32 ms, faster than 23.73% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
# Comment: NA
# -----------------------------------------------------------

def climbStairs(n: int) -> int:
    memo = {1:1, 2:2}
    if n in memo.keys():
        return memo[n]
    else:
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
