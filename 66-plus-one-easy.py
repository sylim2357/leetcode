# -----------------------------------------------------------
# First Attempt
# Runtime: 36 ms, faster than 15.60% of Python3 online submissions for Plus One.
# Memory Usage: 14.1 MB, less than 5.13% of Python3 online submissions for Plus One.
# Comment: NA
# -----------------------------------------------------------

def plusOne(digits: List[int]) -> List[int]:
    carry = False
    answer = []
    for i in range(len(digits)-1,-1,-1):
        if carry | (i==len(digits)-1):
            new_digit = digits[i] + 1
        else:
            new_digit = digits[i]
        carry = False
        if new_digit >= 10:
            carry = True
            new_digit = new_digit - 10
        answer = [new_digit] + answer
    if carry:
        answer = [1] + answer
    return answer
