"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""

from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.isMatchHelper(s, p, s_start = 0, p_start = 0)

    def isMatchHelper(self, s: str, p: str, s_start: int, p_start: int):
        if p_start == len(p):
            return s_start == len(s)
        if p_start + 1 < len(p) and p[p_start + 1] == '*':
            # this replace *c with empty string
            return self.isMatchHelper(s, p, s_start, p_start + 2) \
                or ( s_start < len(s) and (s[s_start] == p[p_start] or p[p_start] == '.') \
                and self.isMatchHelper(s, p, s_start + 1, p_start) )                
        else:
            return s_start < len(s) \
            and (s[s_start] == p[p_start] or p[p_start] == '.') \
            and self.isMatchHelper(s, p, s_start + 1, p_start + 1)

def test():
    sol = Solution()

    s = "aa"
    p = "a*"
    ans = sol.isMatch(s, p)
    assert ( ans == True)


    s = "aa"
    p = "a"
    ans = sol.isMatch(s, p)
    assert (ans == False)


test()





