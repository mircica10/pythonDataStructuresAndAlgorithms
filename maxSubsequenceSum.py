"""
Se dă un vector. Să se găsească o subsecvență (continuă) de sumă maximă.
"""
import math as math

class Solution:
    def __init__(self, arr):
        self.arr = arr

    def solve(self):
        max_sum = -math.inf
        curr_sum = 0
        for element in self.arr:
            curr_sum = max(0, curr_sum + element)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    # get the indexes also
    def solveWithIndexes(self):
        curr_start, curr_end = 0, 0
        best_start, best_end = 0, 0
        max_sum = -math.inf
        curr_sum = 0
        for curr_end, element in enumerate(self.arr):
            if curr_sum > 0:
                curr_sum += element            
            else:                
                curr_start = curr_end
                curr_sum = element

            if curr_sum > max_sum:
                max_sum = curr_sum
                best_start = curr_start
                best_end = curr_end

        return (max_sum, best_start, best_end)


            



    
def test():
    arr = [-5, 4, -8, 1, 2, 3, -1]
    correct_sum = 6
    sol = Solution(arr)
    sum = sol.solve()
    assert ( sum == correct_sum)

    sum, start, end = 6, 3, 5
    (s, st, en) = sol.solveWithIndexes()
    assert((sum, start, end) == (s, st, en) )

test()
