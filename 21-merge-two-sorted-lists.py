# -----------------------------------------------------------
# Failure. Need Review
# Runtime: 32 ms, faster than 86.23% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
# Comment: NA
# -----------------------------------------------------------

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    answer = ListNode()
    temp = answer
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return answer.next
