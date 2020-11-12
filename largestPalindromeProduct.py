"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.
"""
from math import sqrt

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        maxim = 10**n - 1
        mod = 10**n
        
        left = maxim
        #we compose maxim palindrome of length 2n by taking array of length n descendent
        while left > 10**(n - 1):
            #number is a palindrom
            number = left * mod + int(str(left)[::-1])                
            i = maxim
            #test if number is product of  numbers, one being in interval ( maxim, sqrt(number) )
            while i > sqrt(number):
                if number % i == 0:
                    return number % 1337
                i -= 1   
            left -= 1

def test():
    n = 2
    sol = Solution()
    answer = sol.largestPalindrome(n)
    correct_answer = 987
    assert(correct_answer == answer)

test()