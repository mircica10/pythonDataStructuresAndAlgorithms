"""
http://campion.edu.ro/arhiva/index.php?page=problem&action=view&id=1588
"""

class Pseudobil():
    def __init__(self, matrix, D):
        self.matrix = matrix
        self.D = D
        self.rotate = []
        self.n = len(self.matrix)
        self.precalc = []
        self.isPrecalcDone = False
            

    def convert(self, line, col):
        n = self.n
        newLine = line + col
        newCol = col - line + (n - 1)
        return (newLine, newCol)

    def calcRotateMatrix(self):
        n = self.n
        self.rotate = [ [ 0 for _ in range(3 * n)] for _ in range(3 * n)]

        for i in range(n):
            for j in range(n):
                line, col = self.convert(i, j)
                self.rotate[line][col] = self.matrix[i][j]

    # precalculam dr-ul de lungime D
    def precalculate(self):
        self.calcRotateMatrix()

        n = self.n

        self.precalc = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                # aici precalculam, [i][j] fiind coltul din dreapta sus al matricii rotite
                # precalculam pe lungime D
                (upper_right_line, upper_right_col) = self.convert(i, j)

                balls_num = 0
                # D + 1 length of the rotate matrix
                for line in range(upper_right_line, upper_right_line + self.D + 1):
                    for col in range(upper_right_col - self.D, upper_right_col + 1):
                        if self.rotate[line][col] == 1:
                            balls_num += 1
                            
                self.precalc[i][j] = balls_num



    def answerQuestion(self, i, j):
        if self.isPrecalcDone == False:
            self.precalculate()
            self.isPrecalcDone = True

        return self.precalc[i][j]



def test():
    matrix = [
        [1, 0, 0 , 0, 0, 0],
        [0, 0, 1 , 0, 0, 0],
        [0, 0, 0 , 0, 1, 0],
        [0, 0, 0 , 1, 0, 0],
        [0, 0, 0 , 0, 0, 1],
        [0, 0, 0 , 0, 0, 0]        
        ]
    D = 4
    pseudo = Pseudobil(matrix, D)
    
    tentative = pseudo.answerQuestion(0, 2)
    assert(tentative == 3)
    
    tentative = pseudo.answerQuestion(1, 3)
    assert(tentative == 2)

test()