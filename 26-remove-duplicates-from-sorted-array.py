# -----------------------------------------------------------
# First Attempt
# Runtime: 92 ms, faster than 43.78% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.7 MB, less than 85.25% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Comment: NA
# -----------------------------------------------------------

def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    prev = None
    i = 0
    while True:
        if nums[i] == nums[-1]:
            break
        if nums[i] == prev:
            del nums[i]
        else:
            prev = nums[i]
            i += 1
    return i+1
