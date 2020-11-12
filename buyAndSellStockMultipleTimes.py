"""
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
"""

from typing import List
import numpy

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #dp[i][j] - max profit with i transactions and first j prices
        #self.dp = [[-1 for _ in range(n)] for _ in range(k + 1)]
        return self.dp(k, prices)
    
    def dp(self, k, prices):
        n = len(prices)
        #special case 2 * k >= n
        if 2 * k >= n:
            i = 1
            profit = 0
            while i < len(prices):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
                i += 1
            return profit
        #other cases
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]        
        for i in range(1, k + 1):
            localMax = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + localMax)
                localMax = max(localMax, dp[i - 1][j - 1] - prices[j])
        return dp[k][n - 1]
    
    
    def specialCase(self, k, prices):
        i = 1
        profit = 0
        while i < len(prices):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            i += 1
        return profit

    def memo(self, start:int, k: int, prices: List[int]) -> int:
        #dummy case
        if start >= len(prices) or k <= 0:
            return 0
        if self.dp[k][start] >= 0:
            return self.dp[k][start]
        min = prices[start]
        profit = 0
        start = start + 1
        while start < len(prices):
            elem = prices[start]
            if elem <= min:
                min = elem
            else:
                temp_profit = elem - min
                temp_profit += self.memo(start, k - 1, prices)
                profit = max(profit, temp_profit)
            start += 1
        self.dp[k][start] = profit    
        return profit
        

    def back(self, start:int, k: int, prices: List[int]) -> int:
        #dummy case
        if start >= len(prices) or k <= 0:
            return 0
        min = prices[start]
        profit = 0
        start = start + 1
        while start < len(prices):
            elem = prices[start]
            if elem <= min:
                min = elem
            else:
                temp_profit = elem - min
                temp_profit += self.back(start, k - 1, prices)
                profit = max(profit, temp_profit)
            start += 1
        return profit

def test():
    sol = Solution()
    prices = [2,4,1]
    k = 2
    correct_answer = 2
    answer = sol.maxProfit(k, prices)
    assert(answer == correct_answer)

    prices = [3,2,6,5,0,3]
    k = 2
    correct_answer = 7
    answer = sol.maxProfit(k, prices)
    assert(answer == correct_answer)

test()


