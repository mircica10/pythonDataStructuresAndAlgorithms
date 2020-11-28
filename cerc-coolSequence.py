"""
7 4 5 6 8 4 5 7 4 3 2
"""


import math as math

class CoolSequence():
    def __init__(self, array, maxN, maxK):
        self.array = array
        self.maxN = maxN
        self.maxK = maxK
        
    def isSequenceCool(self, i, j):
        vc = [0] * self.maxN
        
        minim = math.inf
        maxim = -math.inf
        
        for index in range(i, j):
            curr = self.array[index]
            if vc[curr] != 0:
                return False
            vc[curr] =  1
            minim = minim if curr >= minim else curr  
            maxim = maxim if curr <= maxim else curr  

        return (maxim - minim) == (j - i - 1)    

    def findMaxSequenceCool(self):
        maxSeqLength = 1
        nrMaxSeq = 1

        for i in range(len(self.array)):
            maxim = -math.inf
            minim = math.inf
            # vector caracteristic
            vc = [0] * self.maxN
            vc[self.array[i]] = 1

            for j in range(i + 1, len(self.array)):
                curr = self.array[j]
                if vc[curr] != 0:
                    break
                
                vc[curr] = 1
                
                minim = minim if curr >= minim else curr  
                maxim = maxim if curr <= maxim else curr  
                # cool sequence
                if maxim - minim == j - i:
                    seqLength = maxim - minim + 1
                    if seqLength == maxSeqLength:
                        nrMaxSeq += 1
                    elif seqLength > maxSeqLength:
                        maxSeqLength = seqLength
                        nrMaxSeq = 1
        
        return (maxSeqLength, nrMaxSeq)


def test():
    a = [7, 4, 5, 6, 8, 4, 5, 7, 4, 3, 2]  
    maxN = 5000
    maxK = 1000
    answer = (5, 2)
    sol = CoolSequence(a, maxN, maxK)
    tentative = sol.findMaxSequenceCool()
    assert(answer == tentative)

    tentative2 = sol.isSequenceCool(0, 4)
    assert (tentative2 == True)
    tentative3 = sol.isSequenceCool(0, 5)
    assert (tentative3 == True)
    tentative3 = sol.isSequenceCool(0, 6)
    assert (tentative3 == False)
    

test()
    

