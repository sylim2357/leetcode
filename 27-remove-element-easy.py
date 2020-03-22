# -----------------------------------------------------------
# Failure. Need Review
# Runtime: 24 ms, faster than 96.15% of Python3 online submissions for Remove Element.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove Element.
# Comment: NA
# -----------------------------------------------------------

def removeElement(nums: List[int], val: int) -> int:
    i = 0
    if len(nums) == 0:
        return 0
    while True:
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
        if len(nums) == i:
            break
    return len(nums)
