"""
Held-Carp algorithm
f(set, n) - min value of tour set ending in n

f( {1, 2, 3,4, 5, 6, 8}, 3)= 
    minimum (
        f( {1, 2, 4, 5, 6, 8}, 2)+ edge(2 →3) ,
        f( {1, 2, 4, 5, 6, 8}, 4)+ edge(4→ 3) ,
        f( {1, 2, 4, 5, 6, 8}, 5)+ edge(5→ 3) ,
        f( {1, 2, 4, 5, 6, 8}, 6)+ edge(6→ 3) ,
        f( {1, 2, 4, 5, 6, 8}, 8)+ edge(8→ 3)    
    )
    this is dp buttom up
"""

import math as math
from typing import List
import itertools

class Solution:
    def travelingSalesmanBottomUpHeldCarp(self, adjacencyMatrix: List[List[int]]) -> int:
        n = len(adjacencyMatrix)
        cache = {}
        # we solve the sets of size 1
        for k in range(1, n):
            cache[(1 << k, k)] = (adjacencyMatrix[k][0], 0)
        # we solve the sets from smaller to bigger
        for subset_size in range(2,n):
            for subset in itertools.combinations(range(1, n), subset_size):
                bits = 0
                for bit in subset:
                    bits |= 1 << bit
                
                for k in subset:
                    prev = bits & ~(1 << k)

                    res = []
                    for m in subset:
                        if m == k:
                            continue
                        res.append((cache[(prev, m)][0] + adjacencyMatrix[m][k], m))
                    cache[(bits,k)] = min(res)
    
        bits = (2**n - 1) - 1
        res = []
        for k in range(1, n):
            res.append((cache[(bits, k)][0] + adjacencyMatrix[k][0], k))
        
        opt, parent = min(res)
        return opt

    def travelingSalesmanTopDown(self, adjacencyMatrix: List[List[int]]) -> int:
        self.adjacencyMatrix = adjacencyMatrix
        self.n = len(adjacencyMatrix)
        self.mem = [[-1 for _ in range( 1 << self.n)] for _ in range(self.n)]
        # no city visited and ended at 1
        return self.tsp(0, 0)

    def tsp(self, i, mask):        
        # all the cities visited, so return the cost from city i to 1
        if mask == ((1 << self.n) - 1):
            return self.adjacencyMatrix[i][0]
        # if in cache, return the result
        if self.mem[i][mask] != -1:
            return self.mem[i][mask]
        res = math.inf
        for j in range(self.n):
            if mask & (1 << j):
                continue
            res = min(res, self.adjacencyMatrix[i][j] + self.tsp(j, mask | (1 << j)))
        # save result in cache
        self.mem[i][mask] = res
        return res
    

    def travelingSalesmanBottomUp(self, adjacencyMatrix: List[List[int]]) -> int:
        n = len(adjacencyMatrix)
        # dp[m][n] - m is the bitmask ending in vertex n
        dp = [[math.inf for _ in range(n)] for _ in range(1 << n)]
        # base case
        for i in range(0, n):
            dp[1 << i][i] = adjacencyMatrix[0][i]
        # iterate over all states
        for mask in range(1, (1 << n) + 1):
            # compute previous state
            for last in range(0, n):
                # last vertex is not in the subset, so continue
                if ((mask >> last) & 1) == 0:
                    continue
                # vertices visited before reaching last
                prev = mask - (1 << last)
                # v represents the possible last locations we could visit in visiting each vertex in prev
                for v in range(0, n):
                    # n vertex is not in prev
                    if ((prev >> v) & 1) == 0:
                        continue
                    currScore = dp[prev][v] + adjacencyMatrix[v][last]
                    dp[mask][last] = min(dp[mask][last], currScore)
        # get min 
        minimum = math.inf
        for i in range(n):
            minimum = min(minimum, dp[(1 << n) - 1][i] + adjacencyMatrix[i][0])
        return minimum

def test():
    sol = Solution()
    adjacencyMatrix = [[ 0, 10, 15, 20 ],
                       [ 10, 0, 35, 25 ],
                       [ 15, 35, 0, 30 ],
                       [ 20, 25, 30, 0 ]]
    result = sol.travelingSalesmanBottomUp(adjacencyMatrix)
    assert (result == 80)

    result = sol.travelingSalesmanTopDown(adjacencyMatrix)
    assert ( result == 80)

    result = sol.travelingSalesmanBottomUpHeldCarp(adjacencyMatrix)
    assert ( result == 80)
    

test()

