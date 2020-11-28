"""
Se dă un vector nesortat; să se găsească distanța maximă între două elemente consecutive în 
vectorul sortat.

Soluția naivă sortează vectorul, deci este O(n log n).

Soluția în O(n) folosește principiul cutiei (principiul lui Dirichlet):

    Găsește minimul și maximul, min și max.
    Împarte (conceptual) intervalul [min-max] în n-1 intervale.
    Plasează cele n-2 numere (fără min și max) în intervale
    La fiecare plasare, actualizează minimul și maximul pentru fiecare interval. 
    Acestea pot fi nule dacă un interval este gol.
    Deoarece există n-2 numere și n-1 intervale, trebuie să existe un interval gol.
    Așadar, distanța maximă va fi precis cel puțin de mărimea unui interval. 
    Ea nu poate apărea între două numere din același interval.
    Parcurge intervalele de la stânga la dreapta și returnează distanța maximă dintre 
    maximul unui interval și minimul următorului interval care nu este gol.
"""

import math as math

class MaximumGap():
    def __init__(self, vector):
        self.vector = vector

    def solve(self):
        boxes = self.composeMinAndMax()
        max_consecutive = -math.inf
        #  left is the max of the preceding element
        minim = min(self.vector)
        maxim = max(self.vector)
        left = minim
        
        for box in boxes:
            if left != None and box[0] != None:
                max_consecutive = max(max_consecutive, box[0] - left)
            if box[1] != None:
                left = box[1]
        
        # check the last value
        if left != None:
            max_consecutive = max(max_consecutive, maxim - left)
        
        return max_consecutive

    def composeMinAndMax(self):
        n = len(self.vector)
        boxes = [(None, None) for _ in range(n - 1)]
        minim = min(self.vector)
        maxim = max(self.vector)
        length_interval = (maxim - minim) // (n - 1)
        # find min and max for all intervals
        for curr in self.vector:
            if curr == minim or curr == maxim:
                continue
            
            index = (curr - minim - 1) // length_interval
            
            (curr_min, curr_max) = boxes[index]
            # default case
            if curr_min == None:
                curr_min = curr
            if curr_max == None:
                curr_max = curr
            
            if curr_min != None and curr < curr_min:
                curr_min = curr
            if curr_max != None and curr > curr_max:
                curr_max = curr
            
            boxes[index] = (curr_min, curr_max)
                
        return boxes 

def test():
    vector = [0, 1,2,3,5,6,7,8,9,10]
    solution = 2
    tentative = MaximumGap(vector).solve()
    assert(solution == tentative)

    vector = [1,3,4,6,7,8,19,22]
    solution = 11
    tentative = MaximumGap(vector).solve()
    assert(solution == tentative)


test()