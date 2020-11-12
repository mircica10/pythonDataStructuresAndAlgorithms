"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
"""


class Solution:
    def minCut(self, s: str) -> int:
        self.dp = [-1 for _ in range(len(s))]
        return self.helper(s, 0)
    
    def helper(self, s, i):
        if self.isPalindrome(s[i:]):
            return 0
        result = len(s[i:]) - 1
        for k in range(i + 1, len(s)):
            if self.isPalindrome(s[i:k]):
                if self.dp[k] == -1:
                    self.dp[k] = 1 + self.helper(s, k)
                result = min(result, self.dp[k]) 
        return result

    def isPalindrome(self, s):
        return s == s[::-1]

def test():
    sol = Solution()
    s = "aab"
    correct_result = 1
    result = sol.minCut(s)
    assert(result == correct_result)

    s = "a"
    correct_result = 0
    result = sol.minCut(s)
    assert(result == correct_result)

    s = "ab"
    correct_result = 1
    result = sol.minCut(s)
    assert(result == correct_result)

    s = "cdd"
    correct_result = 1
    result = sol.minCut(s)
    assert(result == correct_result)

    s = "cabababcbc"
    correct_result = 3
    result = sol.minCut(s)
    assert(result == correct_result)

test()
#print("asc"[1:2])



