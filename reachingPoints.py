"""
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a 
sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
"""

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        return self.solveModulo(sx, sy, tx, ty)

    def solveModulo(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
             sy == ty and sx <= tx and (tx - sx) % sy == 0

    def solveBackwards(self, sx, sy, tx, ty):
        while True:
            if sx == tx and sy == ty:
                return True
            if sx > tx or sy > ty:
                return False
            if tx > ty:
                tx = tx - ty
            else:
                ty = ty - tx


    def solveRecursive(self, sx, sy, tx, ty):
        self.cache = {}
        return self.dp(sx, sy, tx, ty)

    def dp(self, sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return True
        if sx > tx or sy > ty:
            return False
        if (sx, sy) in self.cache:
            return self.cache[sx, sy]
        else:
            self.cache[sx, sy] = self.dp(sx + sy, sy, tx, ty) or self.dp(sx, sx + sy, tx, ty)
            return self.cache[sx, sy]



def test():
    sx, sy, tx, ty = 1, 1, 3, 5
    correct_answer = True
    sol = Solution()
    answer = sol.reachingPoints(sx, sy, tx, ty)
    assert(correct_answer == answer)

    sx, sy, tx, ty = 1, 1, 2, 2
    correct_answer = False
    sol = Solution()
    answer = sol.reachingPoints(sx, sy, tx, ty)
    assert(correct_answer == answer)

    sx, sy, tx, ty = 2, 3, 7, 12
    correct_answer = True
    sol = Solution()
    answer = sol.reachingPoints(sx, sy, tx, ty)
    assert(correct_answer == answer)

test()
