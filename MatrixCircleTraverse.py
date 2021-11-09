
"""
given a matrix, print elements in circle order: 
e.g. : 1 2 3   -> 1 2 3 6 9 8 7 4 5
       4 5 6
       7 8 9
"""

class MatrixCircleTraverse():
    def __init__(self):
        pass

    def solve(self, matrix):
        solution = []
        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, 0
        width, length = m , n    

        upperLeft = matrix[i][j]
        lowerRight = matrix[i + width - 1][j + length - 1]

        while i + width - 1 >= 0 and j + length - 1 >= 0:
            	# upper line
                for col in range(j, j + length):
                    solution.append(matrix[i][col])
                # right line
                for line in range(i + 1, i + width):
                    solution.append(matrix[line][j + length - 1])
                # lower line
                for col in reversed(range(j, j + length - 1)):
                    solution.append(matrix[i + width - 1][col])
                # left line
                for line in reversed(range(i + 1, i + width - 1)):
                    solution.append(matrix[line][j])
                i = i + 1
                j = j + 1
                width = width - 2
                length = length - 2
        
        return solution
    
def test():
    matrix = [[1,2,3,4],[5,6,7,8],[9, 10, 11, 12], [13,14,15,16]]
    r = MatrixCircleTraverse()
    sol = r.solve(matrix)
    correct = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    assert(correct == sol)

test()







