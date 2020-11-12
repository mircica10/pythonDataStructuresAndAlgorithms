"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twosums(self, nums, target):
        hash = {}
        ind = 0
        for num in nums:
            if target - num in hash:#we found solution
                return hash[target - num], ind
            elif not(num in hash):
                    hash[num] = ind
            ind = ind + 1        
        return (-1, -1)        

def test():
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    assert(sol.twosums(nums, target) == (0,1))

test()