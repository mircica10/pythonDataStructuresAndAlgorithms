"""
You are given an array points, an integer angle, and your location, where location = [posx, posy] 
and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Return the maximum number of points you can see
"""

from typing import List
import math as math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        location_points = 0
        angles = []
        for p in points:
            if p[0] == location[0] and p[1] == location[1]:
                location_points += 1                
            else:
                angles.append(math.atan2(p[1] - location[1], p[0] - location[0]))
        # atan2 returns the angle in radians
        angles.sort()
        angles = angles + [x + 2 * math.pi for x in angles]
        #angle in radians
        angle = math.pi * angle / 180
        
        max_points = 0
        left = 0
        
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_points = max(max_points, right - left + 1)

        return max_points + location_points         

    def calculateAngle(self, a, b, c):
        tan1 = math.atan2(c[1] - b[1], c[0] - b[0])
        tan2 = math.atan2(a[1] - b[1], a[0] - b[0])
        angle = math.degrees(tan1 - tan2)
        angle = angle if angle >= 0 else 360 + angle
        return angle

    """
    calculate angle between 3 points
    ba * bc / |ba| * |bc|
    ba = a - b
    |ba| = ba_mod
    """
    def calculateSmallAngle(self, a, b, c):
        ba = [a[0] - b[0], a[1] - b[1]]
        bc = [c[0] - b[0], c[1] - b[1]]
        ba_mod = math.sqrt(ba[0] * ba[0] + ba[1] * ba[1])
        bc_mod = math.sqrt(bc[0] * bc[0] + bc[1] * bc[1])
        cos = (ba[0] * bc[0] + ba[1] * bc[1]) / (ba_mod * bc_mod)
        radians = math.acos(cos)
        angle = math.degrees(radians)
        return angle

    


def test():
    sol = Solution()
    points, angle, location = [[2,1],[2,2],[3,3]], 90, [1,1]
    answer = sol.visiblePoints(points, angle, location)
    assert(answer == 3)

    points, angle, location = [[2,1],[2,2],[3,4],[1,1]], 90, [1,1]
    answer = sol.visiblePoints(points, angle, location)
    assert(answer == 4)

    points, angle, location = [[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]], 0, [1,1]
    answer = sol.visiblePoints(points, angle, location)
    assert(answer == 4)

    points, angle, location = [[956,232],[438,752],[595,297],[508,143],[111,594],[645,824],[758,434],[447,423],[825,356],[807,377]], 38, [74,581]
    answer = sol.visiblePoints(points, angle, location)
    assert(answer == 7)

test()
        