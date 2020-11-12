"""
Given N axis-aligned rectangles where N > 0, determine if they all together form 
an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. 
For example, a unit square is represented as [1,1,2,2]. 
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""

from typing import List
import math as math

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        left_lower_corner, right_upper_corner = (math.inf, math.inf), (-math.inf, -math.inf) 
        area = 0
        countCorners = {}
        for rectangle in rectangles:
            #get lower left and upper right points of the big rectangle
            left_lower_corner = ( min(left_lower_corner[0], rectangle[0]), min(left_lower_corner[1], rectangle[1]) )
            right_upper_corner = ( max(right_upper_corner[0], rectangle[2]), max(right_upper_corner[1], rectangle[3]) )
            #incremental area of small rectangles
            area += (rectangle[2] -rectangle[0]) * (rectangle[3] - rectangle[1])
            
            p1 = (rectangle[0], rectangle[1])
            p2 = (rectangle[2], rectangle[3])
            p3 = (rectangle[2], rectangle[1])
            p4 = (rectangle[0], rectangle[3])
            
            points = [p1, p2, p3, p4]
            for point in points:
                if point in countCorners:
                    countCorners[point] += 1
                else:
                    countCorners[point] = 1
        #needs to be 4 corners with 1 and the rest with 4 or 2
        #those with 1 needs to be the corner of the big rectangle
        cornersWithOne = 0

        for key in countCorners:
            if countCorners[key] == 1:
                cornersWithOne += 1
                #if a corner with one is not a corner of the big rectangle, return False
                if key not in [left_lower_corner, right_upper_corner, (left_lower_corner[0], right_upper_corner[1]), (right_upper_corner[0], left_lower_corner[1])]:
                    return False
            elif countCorners[key] == 2 or countCorners[key] == 4:
                continue
            else:
                return False

        big_rectangle_area = (right_upper_corner[0] - left_lower_corner[0]) * (right_upper_corner[1] - left_lower_corner[1])
        return cornersWithOne == 4 and area == big_rectangle_area

def test():
    sol = Solution()
    rectangles = [[1,1,3,3], [3,1,4,2], [3,2,4,4], [1,3,2,4], [2,3,3,4]]
    answer = sol.isRectangleCover(rectangles)
    assert (answer == True)


    rectangles = [[1,1,2,3], [1,3,2,4], [3,1,4,2], [3,2,4,4]]
    answer = sol.isRectangleCover(rectangles)
    assert (answer == False)

    rectangles = [ [1,1,3,3], [3,1,4,2], [1,3,2,4],  [3,2,4,4]]
    answer = sol.isRectangleCover(rectangles)
    assert ( answer == False)

    rectangles = [[0,0,1,1],[0,0,2,1],[1,0,2,1],[0,2,2,3]]
    answer = sol.isRectangleCover(rectangles)
    assert ( answer == False)


test() 
