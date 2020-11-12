"""
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.
"""
from typing import List
from math import log2

"""
solution is just like the sparse Tree
dp[i][j] - will hold the value of the 2**j parent for node i
"""

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n))
        self.dp = [[-1] * m for _ in range(n)]
        
        for j in range(m):
            for i in range(n):
                if j == 0:
                    self.dp[i][j] = parent[i]
                elif self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            j = int(log2(k))
            node = self.dp[node][j]
            k -= (1 << j)
        return node

        
def test():
    n = 7
    parent = [-1,0,0,1,1,2,2]
    sol = TreeAncestor(n, parent)
    
    node, k = 3, 1
    answer = sol.getKthAncestor(node, k)
    correct_answer = 1
    assert(answer == correct_answer)

    node, k = 5, 2
    answer = sol.getKthAncestor(node, k)
    correct_answer = 0
    assert(answer == correct_answer)

    
    node, k = 6, 3
    answer = sol.getKthAncestor(node, k)
    correct_answer = -1
    assert(answer == correct_answer)

test()

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
