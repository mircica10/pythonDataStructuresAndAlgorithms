"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""

from math import inf
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.solveOptimal(nums)

    def solveOptimal(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n < 1:
            return 0
        l = 0
        r = nums[0]
        step = 1
        maxim = -inf
        while l <= r:
            if r >= n:
                return step

            maxim = -inf
            for i in range(l, r + 1):
                maxim = max(maxim, i + nums[i])
                
            if r > maxim:
                return -1
            l = r
            r = maxim
            step = step + 1
                  

    def solveWithAdditionalSpace(self, nums:List[int]) -> int:
        n = len(nums)
        temp = [inf] * n
        temp[0] = 0
        for idx, val in enumerate(nums):
            counter = 1
            while counter <= val and counter + idx < n:
                temp[counter + idx] = temp[idx] + 1 if temp[counter + idx] > temp[idx] + 1 else temp[counter + idx]
                counter = counter + 1
        return temp[n - 1]


def test():
    nums = [2,3,1,1,4]
    sol = Solution()
    correct = 2
    tentative = sol.jump(nums)
    assert(correct == tentative)

    nums = [2,3,0,1,4]
    correct = 2
    tentative = sol.jump(nums)
    assert(correct == tentative)
    
    nums = [1,2]
    correct = 1
    tentative = sol.jump(nums)
    assert(correct == tentative)
    

test()
