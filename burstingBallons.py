"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Input: [3,1,5,8]
Output: 167 

"""
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        self.memo = [ [ 0 for _ in range(len(nums))] for _ in range(len(nums))] 
        return self.burst(nums, 0, len(nums) - 1)

    def burst(self, nums: List[int], left, right) -> int:
        if left > right:
            return 0
        if self.memo[left][right] > 0:
            return self.memo[left][right]
        ans = 0
        for i in range(left + 1, right):
            temp_ans = nums[left] * nums[i] * nums[right] \
                + self.burst(nums, left, i) + self.burst(nums,  i, right)
            if temp_ans > ans:
                ans = temp_ans
        self.memo[left][right] = ans
        return ans

    
def test():
    sol = Solution()
    a = [3,1,5,8]
    ans = sol.maxCoins(a)
    ans_correct = 167 
    assert (ans == ans_correct)

test()








