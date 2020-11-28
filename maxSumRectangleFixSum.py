"""
Dreptunghiul de sumă maximă de dimensiune p x q

Ca mai sus, dar dreptunghiul găsit trebuie să aibă o dimensiune impusă, p x q.

Soluția naivă este în O(n4), căci sunt O(n2) dreptunghiuri și fiecare se calculează în O(n2).

Pentru o soluție în O(n2), trebuie să precalculăm toate sumele de p elemente pe linie, respectiv q pe coloană. Apoi putem deplasa dreptunghiul la dreapta și în jos în O(1).

O altă variantă, ca și mai sus, este să precalculăm sumele parțiale din orice punct, după care putem calcula în O(1) suma oricărui dreptunghi (nu doar a celor de dimensiuni p x q.

Tema de astăzi vă cere să rezolvați problema folosind doar memorie O(p x n), nu O(m x n). 
"""


class MaxSumRectFixed():
    def __init__(self, matrix, p, q):
        self.matrix = matrix
        self.p = p
        self.q = q
        self.preCalcRows = []
        self.preCalcCols = []

    # p lines
    # q cols
    def preCalc(self):
        self.preCalcRows = [[ 0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0]) - self.q + 1):
                sum_rows = 0
                for k in range(self.q):
                    sum_rows += self.matrix[i][j + k]
                self.preCalcRows[i][j] = sum_rows

    def solve(self):
        self.preCalc()
        curr_sum = 0  
        max_sum = 0
        for i in range(len(self.matrix) - self.p + 1):
            for j in range(len(self.matrix[0]) - self.q + 1):
                curr_sum = sum(self.preCalcRows[i + k][j] for k in range(self.q))
                max_sum = max(max_sum, curr_sum)
        return max_sum

def test():
    matrix = [[-3,3,7,-8], [3,-7,7,-8],[-3,3,77,23],[-3,-12,20,80]]
    p = 2
    q = 2
    sumRect = MaxSumRectFixed(matrix, p, q)
    correct = 200
    tentative = sumRect.solve()
    assert(tentative == correct)

test()