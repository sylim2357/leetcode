# -----------------------------------------------------------
# First Attempt
# Runtime: 52 ms, faster than 31.38% of Python3 online submissions for Roman to Integer.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
# Comment: NA
# -----------------------------------------------------------

def romanToInt(s: str) -> int:
    sym_val_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    bigram_sym_val_list = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}

    num = 0
    i = 0
    while i < len(s):
        if s[i:i+2] in bigram_sym_val_list:
            num += sym_val_dict[s[i+1]] - sym_val_dict[s[i]]
            i += 2
        else:
            num += sym_val_dict[s[i]]
            i += 1
    return num
