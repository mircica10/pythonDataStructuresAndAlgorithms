"""
L(0, n - 1) = L(1, n - 2) + 2, if x[0] == x[n - 1]
            = max(L(1, n - 1), L(0, n - 2)), if x[0] != x[n - 1]

2,3 -> 3,2  2,2  3,3

1,1  1,2  1,3  1,4
2,1  2,2  2,3  2,4
3,1  3,2  3,3  3,4
4,1  4,2  4,3  4,4
"""

class Palindrom():
    def __init__(self, l):
        self.l = l
    
    def solve(self):
        n = len(self.l)
        #init array
        dp = [ 0 for _ in range(n)]
        #init matrix
        for i in range(n):
            dp[i] = ([ 0 for i in range(n)])
        #
        for counter1 in range(n)[::-1]:
            for counter2 in range(n):
                if counter1 <= counter2:
                    #do the math
                    if counter1 == counter2:
                        dp[counter1][counter2] = 1
                    elif self.l[counter1] == self.l[counter2]:
                        dp[counter1][counter2] = dp[counter1 + 1][counter2 - 1] + 2 if counter1 + 1 < n and counter2 - 1 >= 0 else dp[counter1][counter2]#L(0, n - 1) = L(1, n - 2) + 2
                    else:
                        candidate1 = dp[counter1 + 1][counter2] if counter1 + 1 < n else dp[counter1][counter2]
                        candidate2 = dp[counter1][counter2 - 1] if counter2 - 1 >= 0 else dp[counter1][counter2]
                        dp[counter1][counter2] = candidate1 if candidate1 > candidate2 else candidate2               
        return dp#dp[0][n - 1]

def test():
    l = ['b','b', 'a', 'b', 'c', 'b', 'c','a','b']
    pal = Palindrom(l)
    max_palindrome = pal.solve()
    for pol in max_palindrome:
        print(pol)

test()

#for i in range(10)[::-1]:
#    print(i)