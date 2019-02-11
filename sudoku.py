##this program solves sudoku
import math

class Sudoku:

  def __init__(self, size, grid):
    self.size = size
    self.grid = grid

  #helper to define and initialize the variables
  def solveSoduKuHelper(self):
    i = 0
    j = 0
    grid = self.grid
    self.solveSudoku(i, j, grid)       

  def solveSudoku(self, i, j, grid):
    if i == self.size: #we have a solution
      self.printGrid(grid)
      return

    newI = i
    newJ = j

    if j == (self.size - 1): #new indexes 
      newJ = 0
      newI = i + 1
    if j < (self.size - 1):
      newJ = j + 1

    if grid[i][j] > 0: #the cell is ocupied already from the hypothesis
      self.solveSudoku(newI, newJ, grid) 
    if grid[i][j] == 0: #the cell is not occupied
      for k in range(self.size): # values can be from 1 to Size
        grid[i][j] = k + 1
        if self.validPosition(grid, i, j):
          self.solveSudoku(newI, newJ, grid)
        grid[i][j] = 0 # backtrack

  def printGrid(self, grid):
    for i in range(self.size):
      line = ' '
      for j in range(self.size):
        line = line + str(grid[i][j]) + ' '
      print(line)
      line = ''  
       

  def validPosition(self, grid, i, j):
    for k in range(self.size): #check line      
      if grid[i][k] > 0 and k != j:
        if grid[i][k] == grid[i][j]:
          return False   
    for k in range(self.size): #check column
      if grid[k][j] > 0 and k != i:
        if grid[k][j] == grid[i][j]:
          return False
    #check square
    #leftUpperI and leftUpperJ will represent the left upper corner of the little square
    #size of the little square
    #we need math.floor to transfort from float to int
    littleSize = math.floor(math.sqrt(self.size))
    leftUpperI = math.floor(i / littleSize)
    leftUpperJ = math.floor(j / littleSize)
    for ii in range(littleSize):
      for jj in range(littleSize):
        indexI = leftUpperI * littleSize + ii
        indexJ = leftUpperJ * littleSize + jj
        if grid[indexI][indexJ] > 0 and indexI != i and indexJ != j and grid[indexI][indexJ] == grid[i][j]:
          return False
    return True          

board = [ [5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]            
        ]
size = 9
sudoku = Sudoku(size, board)
sudoku.solveSoduKuHelper()