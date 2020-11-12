from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.cache = {}
        return self.helper(s, p, 0, 0)
    
    def helper(self, s: List[int], c: List[int], s_start: int, c_start: int):
        #if already in cache, return it
        if (s_start, c_start) in self.cache:
            return self.cache[s_start, c_start]
        res = False
        #case 1: both end of array
        if (len(s) == s_start and len(c) == c_start):
            res = True
        #case 2: one end of array
        elif (len(c) == c_start):
            res = False
        elif (len(s) == s_start):
            res = c[c_start] == '*' and self.helper(s, c, s_start, c_start + 1) 
        #case 3: equal characters
        elif (s[s_start] == c[c_start]):
            res = self.helper(s, c, s_start + 1, c_start + 1)
        #case 4: non-equal, however we have *
        elif (c[c_start] == '*'):
            res = self.helper(s, c, s_start, c_start + 1) or self.helper(s, c, s_start + 1, c_start)
        #case 5: non-equal, however we have ?
        elif (c[c_start] == '?'):
            res = self.helper(s, c, s_start + 1, c_start + 1)
        #memoization
        self.cache[(s_start, c_start)] = res
        return res

def test():
    sol = Solution()
    
    s = "aa"
    p = "a"
    res = sol.isMatch(s, p)
    assert (res == False)
    
    s = "aa"
    p = "*"
    res = sol.isMatch(s, p)
    assert (res == True)
    
    s = "adceb"
    p = "*a*b"
    res = sol.isMatch(s, p)
    assert (res == True)
    
test()

