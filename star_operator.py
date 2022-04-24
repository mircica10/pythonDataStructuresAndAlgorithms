from typing import Tuple, List, Set, Iterable, Optional
#from numpy import divide, prod, traspose
from collections import namedtuple
import random


Digit = int
Row = Tuple[Digit, ...]
Table = List[Row]
Product = int
Products = List[Product]
Puzzle = namedtuple('Puzzle', 'row_prods, col_prods')

p = Puzzle([135,  45,  64, 280, 70],             [3000,   3969,    640])

from operator import floordiv

def fill_one_row(row_prod: Product, col_prods: Products) -> Set[Row]:
    if not col_prods:
        return {()} if row_prod == 1 else set()
    else:
        return { 
            (d, *rest) for d in range(1, 10)
                if (row_prod / d).is_integer() and (col_prods[0] / d).is_integer()
                    for rest in fill_one_row(row_prod // d, col_prods[1:])
        }
        
def fill_one_row_helper(row_prod: Product, col_prods: Products)->[]:
    solutions = []
    solution = []
    def fill_one_row_inner(row_prod: Product, col_prods: Products):
        if not col_prods:
            if row_prod == 1:
                solutions.append(solution[:])        
        else:
            for d in range(1, 10):
                if (row_prod / d).is_integer() and (col_prods[0] / d).is_integer():
                    solution.append(d)
                    fill_one_row_inner(row_prod // d, col_prods[1:])
                    solution.pop()

    fill_one_row_inner(row_prod, col_prods)
    return solutions
    

def solve_yield(n: int, row_prod: Products, col_prods: Products, solution: []):
    if n == len(row_prod):
        yield solution
    else:
        for sol_row in fill_one_row(row_prod[n], col_prods):
            solution.append(sol_row)
            yield from solve_yield(n + 1, row_prod, list(map(floordiv, col_prods, sol_row)), solution)
            solution.pop()

gen = solve_yield(0, p[0], p[1], [])
for sol in gen:
    print(sol)
    

def solve_helper(row_prod: Products, col_prods: Products)->List[Row]:
    solutions = []
    solution = []
    def solve(n: int, row_prod: Products, col_prods: Products):
        if n == len(row_prod):
            solutions.append(solution[:])
        else:
            for sol_row in fill_one_row(row_prod[n], col_prods):
                 solution.append(sol_row)
                 solve(n + 1, row_prod, list(map(floordiv, col_prods, sol_row)))
                 solution.pop()
    solve(0, row_prod, col_prods)
    return solutions

#solutions = solve_helper(p[0], p[1])
#print(solutions)


#test_row = fill_one_row(210, [6615, 15552, 420])


#test_row = fill_one_row_helper(210, [6615, 15552, 420])
#print(test_row)


print({1,2,3} & {1})
