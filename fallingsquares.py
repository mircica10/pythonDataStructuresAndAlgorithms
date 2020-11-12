from typing import List


class Interval(object):
    def __init__(self, left, size):
        self.left = left
        self.size = size
        self.height = size


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        max_heights: List[int] = []
        intervals: List[Interval] = []
        max_height = 0
        res: List[int] = []

        for position in positions:
            interval = Interval(position[0], position[1])
            interval_height = self.maxHeight(intervals, interval, max_heights)
            
            max_height = self.max(interval_height, max_height)

            res.append(max_height)
            max_heights.append(interval_height)
            intervals.append(interval)
            
        return res     

    def maxHeight(self, intervals: List[Interval], new_interval: Interval, max_heights: List[int]) -> int:
        current_height: int = 0
        counter = -1
        for interval in intervals:
            counter += 1
            if interval.left + interval.size - 1 < new_interval.left:
                continue
            if new_interval.left + new_interval.size - 1 < interval.left:
                continue
            current_height = self.max(max_heights[counter], current_height)
            
        current_height += new_interval.height
        return current_height

    def max(self, a, b):
        return a if a > b else b

def test():
    intervals: List[List[int]] = [[1,2],[2,3],[6,1]]

    sol = Solution()
    answer = sol.fallingSquares(intervals)
    print(answer)

test()