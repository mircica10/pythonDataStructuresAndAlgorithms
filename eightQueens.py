def queensHelper():
  solution = []
  queens(0, solution)

def queens(i, solution):
  if( len(solution) == 8):
    printSolution(solution)
  else:
    for x in range(i, 8):
      for y in range(0, 8):
        isValid = valid(x,y,solution)
        if(isValid):
          solution.append((x,y))
          queens(x + 1, solution)
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
