# -----------------------------------------------------------
# First Attempt
# Runtime: 52 ms, faster than 40.41% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.5 MB, less than 98.51% of Python3 online submissions for Search Insert Position.
# Comment: NA
# -----------------------------------------------------------

def searchInsert(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return 0
    for idx, num in enumerate(nums):
        if num >= target:
            return idx
        elif idx == len(nums)-1:
            return idx+1
