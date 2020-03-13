# -----------------------------------------------------------
# Second Attempt
# Runtime: 48 ms, faster than 78.44% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 34.18% of Python3 online submissions for Two Sum.
# Comment: NA
# -----------------------------------------------------------

def twoSum(self, nums: List[int], target: int) -> List[int]:
    diffs = {}
    for idx, num in enumerate(nums):
        if target-num in diffs.keys():
            return [diffs[target-num], idx]
        else:
            diffs[num] = idx
