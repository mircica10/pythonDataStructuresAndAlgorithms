"""
You are given K eggs, and you have access to a building with N floors from 1 to N. 
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
Your goal is to know with certainty what the value of F is.
What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?
"""

from math import inf
from typing import List

class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = {}
        return self.rec(K, N)


    def rec(self, i, j):
        if i == 1:
            return j
        if j == 0 or j == 1:
            return j
        if (i, j) in self.memo:
            return self.memo[i, j]
        lo, hi = 0, j
        while lo < hi:
            mid = lo + (hi - lo) // 2
            left, right = self.rec(i - 1, mid - 1), self.rec( i, j - mid)
            if left < right:
                lo = mid + 1
            else:
                hi = mid
        res = 1 + self.max(self.rec(i - 1, lo - 1), self.rec(i, j - lo))
        self.memo[i, j] = res
        return res 
        

    def dp(self, K: int, N: int) -> int:
        #dp[i][j] - i eggs for j floors
        dp = [[inf for _ in range(N + 1)] for _ in range(K + 1)]
        #dp[i][0] -> 0, dp[1][j] -> j, dp[i][1] -> 1
        for i in range(K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                left, right = 0, j
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[i - 1][mid - 1] < dp[i][j - mid]:
                        left = mid + 1
                    else:
                        right = mid 
                dp[i][j] = 1 + self.max(dp[i - 1][left - 1], dp[i][j - left])
                #for k in range(i, j + 1):
                #    dp[i][j] = self.min(dp[i][j] , 1 + self.max(dp[i - 1][k - 1], dp[i][j - k])
        
        return dp[K][N] 

    def min(self, a, b):
        return a if a < b else b
    def max(self, a, b):
        return a if a > b else b

def test():
    sol = Solution()
    K, N = 2, 6
    res_correct = 3
    res = sol.superEggDrop(K, N)
    assert(res == res_correct)

test()


