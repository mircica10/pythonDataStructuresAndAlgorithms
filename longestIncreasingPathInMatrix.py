"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
"""
from typing import List
from math import inf

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_path: int = 0
        #for memoization
        cache: List[List[int]] = [[] for _ in range(len(matrix))]
        #init cache with 0
        for i in range(len(matrix)):
            cache[i] = [0 for _ in range(len(matrix[0]))]
        #we perform a deep first search
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current_max_path = self.pathBack(i, j, 1, matrix, cache)
                #update global path
                max_path = current_max_path if current_max_path > max_path else max_path
                #print (f'i:{i} j:{j} current_path:{current_max_path}')
        return max_path

    
    def pathBack(self,row: int, col: int, k: int, matrix: List[List[int]], cache: List[List[int]]):
        #if in cache, we simply return th value in cache
        if cache[row][col] != 0:
            return cache[row][col]
        #we can move only up, down, left and right, ergo directions
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        #we keep track of the local max path
        max_path = 1
   
        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            #test if succesor exists
            if (next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0])):
                continue
            #test if succesor is valid
            if (matrix[row][col] >= matrix[next_row][next_col]):
                continue
            #flag the current cell as visited, so no visit in the future 
            #we assume matrix has positive values so we simply multiply cell value with -1
            matrix[row][col] *= -1 
            #classic backtrack
            next_path = 1 + self.pathBack(next_row, next_col, k + 1 , matrix, cache)
            #undo visited flag
            matrix[row][col] *= -1
            #update the local max
            max_path = next_path if next_path > max_path else max_path
        #we save the current cell in cache       
        cache[row][col] = max_path
        return max_path


  


def test():
    nums = [[3,4,5],
            [3,2,6],
            [2,2,1]]
    sol = Solution()
    size = sol.longestIncreasingPath(nums)
    assert(size == 4)

test()