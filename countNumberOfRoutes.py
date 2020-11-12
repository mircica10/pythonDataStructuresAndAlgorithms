"""
You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish.

Since the answer may be too large, return it modulo 10^9 + 7.

"""
from typing import List
import math as math

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # dp[n][fuel] 
        self.dp = [[-1 for _ in range(fuel + 1)] for _ in range(len(locations))]

        return self.helper(locations, start, finish, fuel)

    
    def helper(self, locations, current, finish, fuel):
        if fuel < 0:
            return 0
        if self.dp[current][fuel] != -1:
            return self.dp[current][fuel]
        answer = 0
        if current == finish:
            answer = 1
        for i in range(len(locations)):
            if i != current:
                answer += self.helper(locations, i, finish, fuel - abs(locations[i] - locations[current]))
        answer = answer % (10**9 + 7)
        self.dp[current][fuel] = answer
        return answer


def test():
    locations, start, finish, fuel = [2,3,6,8,4], 1, 3, 5
    sol = Solution()
    answer = sol.countRoutes(locations, start, finish, fuel)
    assert (answer == 4)

test()



