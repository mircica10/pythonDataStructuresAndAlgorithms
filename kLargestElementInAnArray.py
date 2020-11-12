"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element
"""
from typing import List
import random as random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, len(nums) - k)

    def helper(self, nums, left, right, k):
        random_number =  random.randint(left, right)
        self.swap(nums, random_number, right)
        pivot = nums[right]
        i = left
        j = left
        while j < right:
            if nums[j] <= pivot:
                self.swap(nums, i, j)
                i += 1
            j += 1
        self.swap(nums, i, right)
        if i == k:
            return nums[i]
        elif i < k:
            return self.helper(nums, i + 1, right, k)
        else:
            return self.helper(nums, left, i - 1, k)
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        
        


def test():
    sol = Solution()
    nums, k = [3,2,1,5,6,4], 2
    answer = sol.findKthLargest(nums, k)
    #print(answer)
    assert (answer == 5)

    nums , k = [3,2,3,1,2,4,5,5,6], 4
    answer = sol.findKthLargest(nums, k)
    #print (answer)
    assert (answer == 4)

    nums , k = [7,6,5,4,3,2,1], 2
    answer = sol.findKthLargest(nums, k)
    #print (answer)
    assert (answer == 6)




#test()
# 

    