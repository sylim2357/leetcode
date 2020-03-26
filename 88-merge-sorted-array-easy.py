# -----------------------------------------------------------
# First Attempt
# Runtime: 40 ms, faster than 15.20% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
# Comment: Need better solution
# -----------------------------------------------------------

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if (n == 0):
        return
    elif (m == 0):
        del nums1[0:]
        nums1 += nums2
        return
    i = 0
    while i < n + m:
        if nums2[0] <= nums1[i]:
            nums1.insert(i, nums2[0])
            del nums2[0]
            if len(nums2) == 0:
                del nums1[n+m:]
                return
        elif (i == m + n - len(nums2)) & (len(nums2)!=0):
            del nums1[i:]
            nums1 += nums2
            return
        i += 1
