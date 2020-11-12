"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:
Input: [1,3,2,3,1]
Output: 2

Example2:
Input: [2,4,3,5,1]
Output: 3
"""

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], start:int, stop: int) -> int:
        #dp - reverse[a,b] = reverse[a, mij] + reverse[mij+1,b] + sir din a plus sir b
        if start >= stop:
            return 0
        #get middle
        m = start + (stop - start) // 2
        #solve subproblems
        reversePairsLeft = self.helper(nums, start, m)
        reversePairsRight = self.helper(nums, m + 1, stop)
        #count reverse pairs
        reverse_count = 0
        j = m + 1
        i = start
        # if a[i] > 2 * a[j] it means a[i+1]...a[m] also saisfies the condition, as a[i:m+1] is ordered
        # therefore we add for each step m - i + 1 
        while i <= m:
            if j <= stop and nums[i] > 2 * nums[j]:
                j += 1
                reverse_count +=  (m - i + 1)
            else:
                i += 1    
    
        nums[start:stop + 1] = sorted(nums[start:stop + 1])

        return reverse_count + reversePairsLeft + reversePairsRight

def test():    
    a = [2,4,3,5,1]
    sol = Solution()
    ans = sol.reversePairs(a)        
    assert (ans == 3)
    b = [1,3,2,3,1]
    ans2 = sol.reversePairs(b)
    assert ( ans2 == 2)
   
test()


