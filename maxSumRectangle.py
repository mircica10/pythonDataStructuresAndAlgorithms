"""
Se dă o matrice de numere întregi. Să se găsească dreptunghiul de sumă maximă.

Algoritmul naiv funcționează în O(n6): generează toate dreptunghiurile, care sunt O(n4), și îi calculează suma fiecăruia în O(n2).

O îmbunătățire până la O(n4): precalculăm s[i][j] = suma elementelor din dreptunghiul (1, 1) - (i, j). Apoi generăm în continuare toate dreptunghiurile, dar putem calcula suma fiecăruia în O(1).

Putem ajunge la O(n3). Pentru fiecare pereche de rânduri i și j, 
căutăm în O(n) coloanele k și l care ne dau dreptunghiul maxim. 
Pentru aceasta, dorim să calculăm rapid suma elementelor dintre rândurile i și j pe 
fiecare coloană. Facem aceasta observând că actualizarea sumelor de la perechea (i, j) la 
(i, j + 1) se face în O(n). Apoi, pe vectorul de sume, apelăm algoritmul 1D de subsecvență de sumă maximă. 
"""

from maxSubsequenceSum import Solution as maxSubseqSum
import math as math

class MaxSumRectangle():
    def __init__(self, matrix):
        self.matrix = matrix
        self.preCalc = [ [ 0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ] 
    
    # we compese sum over rows (sij - suma in linia i de la coloane 1 la linia j)
    def doPreCalc(self):
        no_rows = len(self.matrix)
        no_cols = len(self.matrix[0])
        for j in range(no_cols):
            self.preCalc[0][j] = self.matrix[0][j]
        for i in range(1, no_rows):
            for j in range(no_cols):
                self.preCalc[i][j] = self.preCalc[i - 1][j] + self.matrix[i][j]  


    def solve(self):
        self.doPreCalc()
        max_sum = -math.inf
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                curr_sums_array = [ self.preCalc[j][k] - self.preCalc[i][k] for k in range(len(self.matrix[0])) ]
                curr_sum = maxSubseqSum(curr_sums_array).solve()
                max_sum = max(max_sum, curr_sum)
        return max_sum

def test():
    matrix = [[-3,3,7,-8], [3,-7,7,-8],[-3,3,77,23],[-3,-12,20,80]]
    sumRect = MaxSumRectangle(matrix)
    correct = 200
    tentative = sumRect.solve()
    assert(tentative == correct)

test()



    