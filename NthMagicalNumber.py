"""
A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.
"""

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        return self.binarySearch(N, A, B)

    def tle(self, N: int, A: int, B: int) -> int:
        a = [A * i for i in range(N + 1)]
        b = [B * i for i in range(N + 1)]
        indexA = indexB = 0
        k = N
        while indexA <= N and indexB <= N:
            if k == 0:
                return min(a[indexA], b[indexB])
            if a[indexA] == b[indexB]:
                indexA += 1
                indexB += 1                
            elif a[indexA] < b[indexB]:
                indexA += 1
            else:
                indexB += 1 
            k -= 1

    def binarySearch(self, N, A, B):
        a, b = A, B
        while b:
            a, b = b, a % b
        l = 0
        r = 10 ** 14
        #least common denominator
        lcm = A * B // a
        while l < r:
            m = l + (r - l) // 2
            if m // A + m // B - m // lcm < N:
                l = m + 1
            else:
                r = m
        
        return l % (10**9 + 7)




        
def test():
    sol = Solution()
    N, A, B = 1, 2, 3
    correct_answer = 2
    answer = sol.nthMagicalNumber(N,A,B)
    assert(correct_answer == answer)

    N, A, B = 4, 2, 3
    correct_answer = 6
    answer = sol.nthMagicalNumber(N,A,B)
    assert(correct_answer == answer)

    N, A, B = 5,2,4
    correct_answer = 10
    answer = sol.nthMagicalNumber(N,A,B)
    assert(correct_answer == answer)

    N, A, B = 3,6,4
    correct_answer = 8
    answer = sol.nthMagicalNumber(N,A,B)
    assert(correct_answer == answer)

test()
