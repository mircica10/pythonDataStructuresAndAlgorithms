"""
Given the integer n representing the number of courses at some university labeled from 
1 to n, and the array dependencies where dependencies[i] = [xi, yi]  
represents a prerequisite relationship, that is, the course xi must be
 taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the
 prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. 
It is guaranteed that you can take all courses in some way.

dp[i][j] - take courses codified as i and ending in j
"""

from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        return self.solveSetBits(n, dependencies, k) 
    
    # similar cu traveling salesman problem
    def solveSetBits(self, n, dependencies, k):
        # dep[i] = j - to take j one msut take i courses
        # i bit-codified the course
        dep = [0] * n
        for dependency in dependencies:
            dep[dependency[1] - 1] |= ( 1 << (dependency[0] - 1) )
        # dp[i] minimum number of semesters one can take i courses, again bit codified
        # initialized with n, as this is the max number 
        dp = [n] * (1 << n)
        # no courses, 0 semester
        dp[0] = 0
        
        for i in range(1 << n):
            #what can we study for i courses taken
            canStudy = 0
            for j in range(n):
                if (i & dep[j]) == dep[j]:
                    canStudy |= (1 << j)                
            # we don't care about i courses, as we want to iterate over all the coruses 
            # which we can take from current stare, namely i
            canStudy &= ~i
            # we want to iterate over all subsets of canStudy
            sub = canStudy
            while sub > 0:
                if bin(sub).count("1") <= k:
                    dp[i | sub] = min(dp[i | sub], dp[i] + 1)
                # this is a way to generate all subsets for bit sets
                sub = (sub - 1) & canStudy

        return dp[(1 << n) - 1] 

    def solveGreedyWrong(self, n: int, dependencies: List[List[int]], k: int) -> int:
        self.list_dependency = {}
        for dependency in dependencies:
            if dependency[1] in self.list_dependency:
                self.list_dependency[dependency[1]].append(dependency[0])
            else:
                self.list_dependency[dependency[1]] = [dependency[0]]
        #add the other course, whoch are not in children or parents
        parents = []
        children = []
        for dependency in dependencies:
            if dependency[1] not in parents:
                parents.append(dependency[1])
            if dependency[0] not in children:
                children.append(dependency[0])
        # add -1 as dummy root
        dummy_root = 0
        self.list_dependency[dummy_root] = []
        for parent in parents:
            if parent not in children:
                self.list_dependency[dummy_root].append(parent)
        # add to dummy root the numbers which are not parents of children
        for i in range(1, n + 1):
            if i not in parents and i not in children:
                self.list_dependency[dummy_root].append(i)
        #construct tree
        current_queue = [dummy_root]
        next_queue = []
        semester_count_total = 0
        while len(current_queue) > 0:
            #the the number or semensters for current level in tree
            semester_count_local = len(current_queue) // k
            if len(current_queue) % k > 0:
                semester_count_local += 1
            # add to the total number of semesters
            semester_count_total += semester_count_local
            #compose the next level in tree
            for current_parent in current_queue:
                if current_parent in self.list_dependency:
                    next_queue = next_queue + self.list_dependency[current_parent]
            # next level becomes the current level
            current_queue = next_queue
            # reset next nevel
            next_queue = []

        # we subtract the dummy root
        return semester_count_total - 1


def test():
    sol = Solution()
    n, dependencies, k = 4, [[2,1],[3,1],[1,4]], 2
    answer = sol.minNumberOfSemesters(n, dependencies, k)
    assert (answer == 3)

    n , dependencies, k = 5, [[2,1],[3,1],[4,1],[1,5]], 2
    answer = sol.minNumberOfSemesters(n, dependencies, k)
    assert (answer == 4)

    n , dependencies, k = 11, [], 2
    answer = sol.minNumberOfSemesters(n, dependencies, k)
    assert (answer == 6)

    
test()


