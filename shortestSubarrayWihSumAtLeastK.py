from typing import List
import heapq
import math

class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        shortest = math.inf 
        sum = 0
        #priority queue to store tuples (partial_sum, index_last_element)
        pq = []
        #we iterate over array
        for counter, value in enumerate(A):
            sum += value
            if sum >= k and counter < shortest:
                shortest = counter + 1 
            # if sum - smallest_partial_sum greater than k, we check the length and pop it,
            # as we'll not need it afterwards (because i - partial_index < i+1 - partial_index) 
            while pq and sum - pq[0][0] >= k:
                if counter - pq[0][1] < shortest:
                    shortest = counter - pq[0][1]
                heapq.heappop(pq)  
                            
            heapq.heappush(pq, (sum, counter))
            
        return shortest if shortest != math.inf else -1

def test():
    sol = Solution()
    A = [2,-1,2]
    k = 3
    result = sol.shortestSubarray(A, k)
    print(result)
  
test()