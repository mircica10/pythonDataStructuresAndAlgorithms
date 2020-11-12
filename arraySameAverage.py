"""
In a given integer array A, we must move every element of A to either list B or list C. 
(B and C initially start empty.)

Return true if and only if after such a move, 
it is possible that the average value of B is equal to the average value of C, 
and B and C are both non-empty.
"""

from typing import List

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        return self.dp_bitwise(A)

    def dp_bitwise(self, A: List[int]) -> bool:
        #dummy case
        if (len(A) <= 1):
            return False
        #calculate sum and number of elements
        n = len(A)
        Sum = 0
        for x in A:
            Sum += x
        #dp[s] = m -- means sum s can be formed with elements of length bit i == 1 of m
        #e.g. dp[10] = 20 it means sum 10 can be achieved with 2 or 4 elements - 10100 
        #init dp with 0
        dp = [ 0 for _ in range(Sum+1)]
        dp[A[0]] = 2
        #we iterate through all the elements
        for i in range(1, n):
            #we check every possible sum 
            for s in range(Sum-A[i], -1, -1):
                #if s can be previously formed
                if dp[s] > 0:
                    #it means we can form s + A[i] also from dp[s] by shifting it with one, as we have an additional element
                    dp[s + A[i]] |= (dp[s]<<1)
            dp[A[i]] |= 2
        
        for leng in range(1, n):
            if (Sum * leng) % n == 0 and ( (1 << leng) & dp[(Sum * leng) // n] ):
                return True
        return False

    def back_helper(self, A):
        self.memo = {}
        sum = 0
        for elem in A:
            sum += elem

        i = 1
        while i < (len(A) // 2 + 1):
            if (sum * i) % len(A) == 0:
                target = i * sum // len(A)
                if self.back_memo(A, target, i, 0):
                    return True
            i += 1    
        return False
        

    def back_memo(self, A, target, nr_remaining_elements, index_searched_elements):
        if nr_remaining_elements == 0:
            return target == 0
        if target < 0 or nr_remaining_elements + index_searched_elements > len(A):
            return False
        if (target, nr_remaining_elements, index_searched_elements) in self.memo:
            return self.memo[(target, nr_remaining_elements, index_searched_elements)]
        res = self.back(A, target, nr_remaining_elements, index_searched_elements + 1) or \
            self.back(A, target - A[index_searched_elements], nr_remaining_elements - 1, index_searched_elements + 1)
        self.memo[(target , nr_remaining_elements , index_searched_elements)] = res
        return res

    def dp(self, A):
        if len(A) == 2:
            return A[0] == A[1]
        sum = 0
        for i in A: 
            sum += i
        
        max_n = 2
        max_k = 16
        max_s = 300001
        #dp[n][k][s] means whether sum s could be achieved by summing up k numbers 
        # selected among the first n numbers in given array.
        dp = [ [ [False for _ in range(max_s)] for _ in range(max_k) ] for _ in range(max_n) ]

        N = len(A)

        for n in range(N + 1):
            dp[n & 1][0][0] = True
        
        for n in range(1, N + 1):
            for k in range(1, N // 2 + 1):
                for s in range(1, sum + 1):
                    if s >= A[n - 1]:
                        dp[n & 1][k][s] = dp[(n - 1) & 1][k][s] or dp[(n - 1) & 1][k - 1][s - A[n - 1]]                        
                    else:
                        dp[n & 1][k][s] = dp[(n - 1) & 1][k][s]   

        for k in range(1, N // 2 + 1):
            if sum * k % N == 0 and dp[N & 1][k][sum * k // N]:
                return True
        
        return False






    def back(self, A, target, nr_remaining_elements, index_searched_elements):
        if nr_remaining_elements == 0:
            return target == 0
        if target < 0 or nr_remaining_elements + index_searched_elements > len(A):
            return False
        return self.back(A, target, nr_remaining_elements, index_searched_elements + 1) or \
            self.back(A, target - A[index_searched_elements], nr_remaining_elements - 1, index_searched_elements + 1)




def test():
    sol = Solution()
    a = [17,3,7,12,1]
    ans = sol.splitArraySameAverage(a)   
    assert(ans == False)


    a = [3,1]
    ans = sol.splitArraySameAverage(a)   
    assert(ans == False)

    
    a = [1,2,3,4,5,6,7,8] 
    ans = sol.splitArraySameAverage(a)   
    assert(ans == True)

    a = [1,5,7,9] 
    ans = sol.splitArraySameAverage(a)   
    assert(ans == False)

    

test()



