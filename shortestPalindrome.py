"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.
"""

from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_modified = s + '#' + s[::-1]
        table = self.constructKmpTable(s_modified)
        max_value = table[len(s_modified)]
        return s[max_value:][::-1] + s[0:max_value] + s[max_value:] 
        #sasbcd -> dcbsasbcd

    def constructKmpTable(self, W):
        T = [0 for _ in range(len(W) + 1)]
        pos = 1
        cnd = 0
        T[0] = -1
        while pos < len(W):
            if W[pos] == W[cnd]:
                T[pos] = T[cnd]
            else:
                T[pos] = cnd
                cnd = T[cnd]
                while cnd >= 0 and W[pos] != W[cnd]:
                    cnd = T[cnd]
            pos += 1
            cnd += 1
        T[pos] = cnd
        return T


    def bruteForce(self, s: str) -> str:
        #check if palindrome has center
        maxim = 0
        for index, elem in enumerate(s):
            if index > len(s) // 2:
                break
            i = 0
            while index - i >= 0 and index + i < len(s):
                if s[index - i] == s[index + i]:
                    i += 1
                else:
                    break
            if index - i + 1 == 0:
                maxim = max(1 + (i - 1) * 2, maxim)
        #check if palindrome has no center
        for index, elem in enumerate(s):
            if index > len(s) // 2 or len(s) == 1:
                break
            i = 0
            while index - i >= 0 and index + 1 + i < len(s):
                if s[index - i] == s[index + 1 + i]:
                    i += 1
                else:
                    break
            if index - i + 1== 0:    
                maxim = max(i * 2, maxim)

        return s[maxim:len(s)][::-1] + s

    def checkPalindrome(self, s):
        if s == s[0] * len(s):
            return True
        return False
               


def test():
    sol = Solution()
    s = "aacecaaa"
    correct_answer = "aaacecaaa"
    answer = sol.shortestPalindrome(s)
    assert(correct_answer == answer)

    s = "abcd"
    correct_answer = "dcbabcd"
    answer = sol.shortestPalindrome(s)
    assert(correct_answer == answer)

    s = "a"
    correct_answer = "a"
    answer = sol.shortestPalindrome(s)
    assert(correct_answer == answer)

    s = "ba"
    correct_answer = "aba"
    answer = sol.shortestPalindrome(s)
    assert(correct_answer == answer)

    s = "ababbbabbaba"#12
    correct_answer = "ababbabbbababbbabbaba"#21
    answer = sol.shortestPalindrome(s)
    assert(correct_answer == answer)


test()