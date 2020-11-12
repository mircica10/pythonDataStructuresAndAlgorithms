"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n))
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return self.aproach2(nums1, nums2)

    def aproach2(self, nums1, nums2):
        """
        does not work for some corner cases, when one array is empty
        x1 x2 x3 | x4 x5

        y1 y2 | y3 y4
        condition: x3 < y3 and y2 < x4

        """
        #we'll work on the small array
        iShort = nums1
        iLong = nums2
        if len(nums1) > len(nums2):
            iShort = nums2
            iLong = nums1

        left  = 0
        right = len(iShort) - 1
        
        #binary search
        while True:
            m = (left + right) // 2#left + (right - left) // 2
            (shortLeft, shortRight, longLeft, longRight) = self.getIndexes(m, iShort, iLong)
            if self.getVal(iShort, shortLeft) > self.getVal(iLong, longRight):
                right = m - 1
            elif self.getVal(iLong, longLeft) > self.getVal(iShort, shortRight):
                left = m + 1
            else:
                return self.composeMedian(shortLeft, shortRight, longLeft, longRight, iShort, iLong)
      
    #check if this function is really needed
    def getVal(self, array, index):
        if index < 0:
            return float('-inf')
        elif index >= len(array):
            return float('inf')
        else:
            return array[index]    

    def getIndexes(self, shortLeft, iShort, iLong):
        longLeft = (len(iShort) + len(iLong) + 1) // 2 - shortLeft - 1
        return (shortLeft, shortLeft + 1, longLeft - 1, longLeft)

    def composeMedian(self, shortLeft, shortRight, longLeft, longRight, iShort, iLong):
        if (len(iShort) + len(iLong) ) % 2 == 0:
            maxLeftArray = self.max(self.getVal(iShort, shortLeft), self.getVal(iLong, longLeft))
            minRightArray = self.min(self.getVal(iShort, shortRight), self.getVal(iLong, longRight)) 
            return ( maxLeftArray + minRightArray ) / 2.0
        else:
            #right array will be +1 bigger due to the "shortLeft - 1" in the getIndexes()
            maxLeftArray = self.max(self.getVal(iShort, shortLeft), self.getVal(iLong, longLeft)) 
            return maxLeftArray


    def min(self, a, b):
        return a if a < b else b

    def max(self, a, b):
        return a if a > b else b    


    def aproach1(self, nums1, nums2):
        result1 = self.findIfMedianInArray(nums1, nums2)
        if (result1 is None):
            return self.findIfMedianInArray(nums2, nums1)
        else:
            return result1
    #we search the median in nums1 only
    def findIfMedianInArray(self, nums1, nums2):
        left = 0
        right = len(nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)

        while left <= right:
            i = left + (right - left) // 2 
            j = ( n2 + n1 + 1 ) // 2 - i

            if i < n1 and j > 0 and nums1[i] < nums2[j - 1]:
                left = i + 1
            elif i > 0  and j < n2 and nums2[j] < nums1[i - 1]:
                right = i - 1
            else:
                if i == 0:
                    median = nums2[j - 1]
                elif j == 0:
                    median = nums1[i - 1]
                else:
                    median = max(nums1[i - 1], nums2[j - 1])
                break
        
        if (n1 + n2) % 2 == 1: 
            return median 
   
        if i == n1: 
            return (median + nums2[j]) / 2.0 
        
        if j == n2: 
            return (median + nums1[i]) / 2.0 
       
        return ( median + min( nums1[i], nums2[j] ) ) / 2.0  




def test():
    s1 = [1, 2]
    s2 = [3, 4]
    sol = Solution()
    median = sol.findMedianSortedArrays(s1, s2)
    assert( median == 2.5)

test()