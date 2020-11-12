"""
Given two arrays of length m and n with digits 0-9 representing two numbers. 
Create the maximum number of length k <= m + n from digits of the two. 
The relative order of the digits from the same array must be preserved. 
Return an array of the k digits.
"""

from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        return []

    def solve(self, a: List[int], b: List[int], k: int) -> List[int]:
        res = []
        for i in range(k + 1):
            if i <= len(a) and k - i <= len(b):
                left = self.stack(a, i)
                right = self.stack(b, k - i)
                temp_res = self.merge(left, right)
                res = max(res, temp_res)
        return res

    #returns a list with biggest k numbers in array, in order
    def stack(self, a: List[int], k: int) -> List[int]:
        stack = []
        remaining = len(a) - k
        for elem in a:
            while len(stack) > 0 and remaining > 0 and stack[-1] < elem:
                stack.pop() # pops the last element in array
                remaining -= 1
            stack.append(elem)
        return stack[:k] # decreasing order array will have stack equal with the original array - no pop() occuring

    # merge 2 arrays in lexicografically order
    # max(a,b) returns the array with the smallest first element
    def merge(self, a, b):
        return [max(a, b).pop(0) for _ in a + b]

    

def test():
    sol = Solution()
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    ans_correct = [9, 8, 6, 5, 3]
    ans = sol.solve(nums1, nums2, k)
    assert (ans == ans_correct)

test()
    


