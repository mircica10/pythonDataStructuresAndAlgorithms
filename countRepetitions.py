"""
Define S = [s,n] as the string S which consists of n connected strings s. 
For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can 
remove some characters from s2 such that it becomes s1. 
For example, “abc” can be obtained from “abdbec” based on our definition, 
but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and 
two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, 
where S1=[s1,n1] and S2=[s2,n2]. 
Find the maximum integer M such that [S2,M] can be obtained from S1.
"""

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # this hold the repetitions
        cache = {}
        l1 , l2 = len(s1), len(s2)
        #indices in n1*s1 and n2*s2
        i, j = 0, 0
        while i < l1 * n1:
            if s1[i % l1] == s2[j % l2]:
                if (i % l1, j % l2) in cache:
                    previousI, previousJ = cache[(i % l1, j % l2)]
                    circleOneLength, circleTwoLength = i - previousI, j - previousJ
                    circleOneCount = (l1 * n1 - i) // circleOneLength
                    i += circleOneCount * circleOneLength
                    j += circleOneCount * circleTwoLength
                else:
                    cache[(i % l1,j % l2)] = (i, j)               
                j += 1
            i += 1
        return j // l2 // n2 

def test():
    sol = Solution()
    s1, n1 = "acb", 4
    s2, n2 ="ab", 2
    correct_answer = 2
    answer = sol.getMaxRepetitions(s1, n1, s2, n2)
    assert (answer == correct_answer)

test()