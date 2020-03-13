# -----------------------------------------------------------
# First Attempt
# Runtime: 84 ms, faster than 14.61% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.
# Comment:
# Guessing the Time Complexity is O(max(n+1, m+1)), should be slower than O(max(n,m)).
# Need varification
# -----------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    count = 0
    num1 = 0
    while l1:
        num1 += l1.val*10**count
        l1 = l1.next
        count += 1
    count = 0
    num2 = 0
    while l2:
        num2 += l2.val*10**count
        l2 = l2.next
        count += 1
    answer = num1 + num2
    for idx, i in enumerate(map(int, str(answer))):
        if idx == 0:
            last_node = ListNode(i)
            answer_node = last_node
        else:
            prev_node = ListNode(i)
            prev_node.next = answer_node
            answer_node = prev_node
    return answer_node
