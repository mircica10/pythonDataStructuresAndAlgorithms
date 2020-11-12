"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return self.getKsmallestElement('', k, n)


    def getKsmallestElement(self, prefix, k, n, start = 0):
        prefix = 1
        k -= 1
        while k > 0:
            count = self.countPrefix(prefix, n)
            if k >= count:
                k -= count
                prefix += 1
            else:
                prefix *= 10
                k -= 1
        return prefix


    def countPrefix(self, prefix, limit):
        count = 0
        l, r = prefix, prefix + 1
        while l <= limit:
            count = count + min(r, limit + 1) - l            
            l = l * 10
            r = r * 10            
        return count
            

    #count numbers that start with prefix in max n
    def countNumbersWithPrefix(self, prefix, upperLimit):
        count = 0
        minim = int(prefix)
        maximum = int(prefix)
        if maximum <= upperLimit: 
            count += 1
        for i in range(1,10):
            minim = int(str(prefix) + '0' * i)#11 + 0 * 2 -> 1100
            maximum = int(str(prefix) + '9' * i)#11 + 9 * 2 -> 1199
            if minim > upperLimit:
                return count
            elif maximum > upperLimit:
                count += upperLimit - minim + 1
                return count
            else:
                count += (maximum - minim + 1)
        return count     


    def tle(self, n, k):
        s = [i for i in range(1, n + 1)]
        s.sort(key= lambda s : str(s).lower())
        return s[k - 1]

def test():
    sol = Solution()
    k = 2
    n = 13
    answer = sol.findKthNumber(n, k)
    correct_answer = 10
    assert (answer == correct_answer)

    k = 2
    n = 2
    answer = sol.findKthNumber(n, k)
    correct_answer = 2
    assert (answer == correct_answer)

    k = 3
    n = 10
    answer = sol.findKthNumber(n, k)
    correct_answer = 2
    assert (answer == correct_answer)

    k = 10000
    n = 10000
    answer = sol.findKthNumber(n, k)
    correct_answer = 9999
    assert (answer == correct_answer)

    

test()
