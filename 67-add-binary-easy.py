# -----------------------------------------------------------
# First Attempt
# Runtime: 40 ms, faster than 12.46% of Python3 online submissions for Add Binary.
# Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Add Binary.
# Comment: NA
# -----------------------------------------------------------

def addBinary(a: str, b: str) -> str:
    temp = str(int(a) + int(b))
    carry = False
    answer = []
    for i in range(len(temp)-1,-1,-1):
        if carry:
            new_digit = int(temp[i]) + 1
        else:
            new_digit = int(temp[i])
        carry = False
        if new_digit >= 2:
            carry = True
            new_digit = new_digit - 2
        answer = [str(new_digit)] + answer
    if carry:
        answer = ['1'] + answer
    return ''.join(answer)
