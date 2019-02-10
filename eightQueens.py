def queensHelper():
  solution = []
  BOARD_SIZE = 4
  queens(0, solution, BOARD_SIZE)

#we don't have to check for i > 8, as if i > 8, it means 8 queens are already on the board so there is no 
#place for a new one, as the loop for j runs until 8 and a new one will be placed on a spot on the same line
#with another one already part of the solution, so the valid function will fail. hence, the test i < 8 is implicit
def queens(i, solution, boardSize):
  if (len(solution) == boardSize):
    printSolution(solution)
  else:
    for j in range(0, boardSize):
      isValid = valid(i, j, solution)
      if(isValid):
        solution.append((i, j))
        queens(i + 1, solution, boardSize)
        solution.pop()

def printSolution(solution):
  print("solution")
  for i in range(0, len(solution)):
    point = solution[i]
    print(f'x:{point[0]} y:{point[1]}')
  print("end solution")

def valid(x, y, solution):
  for i in range(0, len(solution)):
    currentQueen = solution[i]
    if  (currentQueen[0] - x) == 0 or (currentQueen[1] - y) == 0 or ( abs(currentQueen[1] - y) == abs(currentQueen[0] - x) ) :
      return False
  return True

queensHelper()
