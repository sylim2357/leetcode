# -----------------------------------------------------------
# First Attempt
# Runtime: 28 ms, faster than 87.77% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.1 MB, less than 81.90% of Python3 online submissions for Longest Common Prefix.
# Comment: NA
# -----------------------------------------------------------

def longestCommonPrefix(strs: List[str]) -> str:
    answer = ''
    if len(strs) == 0:
        return ''
    else:
        for i in range(min([len(string) for string in strs])):
            if len(set([string[i] for string in strs])) != 1:
                break
            else:
                answer += strs[0][i]
        return answer
