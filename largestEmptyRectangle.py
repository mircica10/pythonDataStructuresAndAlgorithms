"""
Se dă o matrice de 0 și 1. Să se găsească dreptunghiul de arie maximă care conține doar 0. 
"""

class MaxEmptyRectangle():
    def __init__(self, matrix):
        self.matrix = matrix
        self.preCalc = []

    def preprocess(self):
        # self.preCals[i][j] - numarul de zerouri la dreapta de [i][j]
        nr_rows, nr_cols = len(self.matrix), len(self.matrix[0])

        self.preCalc = [[None for _ in range(nr_rows)] for _ in range(nr_cols)]
        
        for i in range(nr_rows):
            for j in range(nr_cols):
                countZeros = 0
                for k in range(j, nr_cols):
                    if self.matrix[i][k] == 0:
                        countZeros += 1
                    else:
                        break
                self.preCalc[i][j] = countZeros
    # O(n**3) complexity
    def getMaxRectangle(self):
        self.preprocess()
        max_area = 0
        nr_rows, nr_cols = len(self.matrix), len(self.matrix[0])

        for i in range(nr_rows):
            for j in range(nr_cols):
                minimum = self.preCalc[i][j]
                for k in range(i, nr_rows):
                    minimum = min(minimum, self.preCalc[k][j])
                    curr_area = (k - i + 1) * minimum
                    max_area = max(max_area, curr_area)
        return max_area

def test():
    matrix = [
        [0,0,4,3],
        [0,0,4,3],
        [0,0,4,3],
        [0,1,4,3]        
    ]
    answer = 6
    tentative = MaxEmptyRectangle(matrix).getMaxRectangle()
    assert (answer == tentative)

    matrix = [
        [0,0,4,3],
        [0,3,4,3],
        [6,0,4,3],
        [0,1,4,3]        
    ]
    answer = 2
    tentative = MaxEmptyRectangle(matrix).getMaxRectangle()
    assert (answer == tentative)

test()
