
"""
Să considerăm o serie de clădiri de diverse înălțimi, stocate într-un vector. 
După ultima clădire este plaja. De pe terasa unei clădiri se poate vedea plaja dacă 
toate clădirile dintre ea și plajă au înălțime strict mai mică decât clădirea în discuție.
 Să se determine toate clădirile de pe care se vede plaja. 
"""

from collections import deque

class Solution():
    def __init__(self, arr):
        self.arr = arr

    def solve(self):
        stack = deque()
        for building in self.arr:
            while len(stack) > 0 and building > stack[-1]:
                stack.pop()
            stack.append(building)
        return list(stack)
                


def test():
    sir = [1, 8, 1, 4, 3, 2, 1, 6, 1, 3, 2, 3, 1, 4, 1]
    correct_ans = [8,6,4,1]
    sol = Solution(sir)
    ans = sol.solve()
    assert(ans == correct_ans)

test()

