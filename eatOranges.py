"""
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

    Eat one orange.
    If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
    If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.

You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.
"""
from math import inf
from typing import List
from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        self.cache = {}
        return self.bfs(n)

    def bfs(self, n: int) -> int:
        q = deque()    
        q.append(n)
        steps = 0
        visited = set()
        visited.add(n)

        while q:
            steps += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr % 3 == 0 and not curr // 3 in visited:
                    q.append(curr // 3)
                    visited.add(curr)
                if curr % 2 == 0 and not curr // 2 in visited:
                    q.append(curr // 2)
                    visited.add(curr)
                if curr - 1 not in visited:
                    q.append(curr // 2)
                    visited.add(curr)
                if curr - 1 == 0:
                    return steps
                

    def memo(self, n: int) -> int:
        if n <= 1:
            return n
        if n in self.cache:
            return self.cache[n]
        res = 1 + min(n% 2 + self.memo(n // 2), n % 3 + self.memo(n // 3))
        self.cache[n] = res
        return res

    def dp(self, n: int) -> int:
        #dp[n] min number of days to eat n oranges
        dp = [inf for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            s1 = dp[i - 1] + 1
            s2 = dp[i - i // 2] + 1 if i % 2 == 0 else s1
            s3 = dp[i - 2 * i // 3] + 1 if i % 3 == 0  else s1
            s = min(s1, min(s2, s3))
            dp[i] = s
        return dp[n]



def test():
    sol = Solution()
    n = 10
    res = sol.minDays(n)
    res_correct = 4
    assert(res == res_correct)
    
    n = 6
    res = sol.minDays(n)
    res_correct = 3
    assert(res == res_correct)
    

test()
    
