# -----------------------------------------------------------
# First Attempt
# Runtime: 20 ms, faster than 97.83% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
# Comment: NA
# -----------------------------------------------------------

def isValid(self, s: str) -> bool:
    if len(s)%2==1:
        return False
    paren_dict = {'(':')', '{':'}', '[':']'}
    paren_list = []
    for char in s:
        if char in paren_dict.keys():
            paren_list.append(paren_dict[char])
        else:
            if len(paren_list) == 0:
                return False
            if paren_list[-1] == char:
                paren_list.pop()
            else:
                return False
    if len(paren_list) == 0:
        return True
    else:
        return False
