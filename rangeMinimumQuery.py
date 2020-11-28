"""
Această problemă intră în categoria clasică a problemelor de preprocesare și interogare 
(preprocessing and query). Se dă un vector de n numere, apoi se pun q întrebări de 
forma „care este elementul minim între pozițiile i și j inclusiv?”
"""

# sunt 4 metode, prezentam 3 aici


import math as math

class RangeMinimumQuery():
    def __init__(self, array):
        self.array = array
        
        self.preprocessing = []
        self.isCompletePreprocesingInitialize = False
        
        self.logPreprocessing = []
        self.isLogPreprocesingInitialize = False
        
        self.sparseTable = []
        self.isSparseTableInitialize = False

    def initCompletePreprocessing(self):
        if not self.isCompletePreprocesingInitialize:
            self.doCompletePreprocessing()
            self.isFullPreprocesingInit = True

    def initLogPreprocessing(self):
        if not self.isLogPreprocesingInitialize:
            self.doLogPreprocessing()
            self.isLogPreprocesingInit = True

    def initSparseTablePreprocessing(self):
        if not self.isSparseTableInitialize:
            self.doSparseTableInitialize()
            self.isSparseTableInitialize = True


    # O(n**2)
    def doCompletePreprocessing(self):
        no_rows = len(self.array)
        no_columns = len(self.array)
        preprocessing = [ [ None for _ in range(no_columns)] for _ in range(no_rows) ]
        
        for i in range(no_rows):
            for j in range(i, no_columns):
                if i == j:
                    preprocessing[i][j] = self.array[i]
                else:
                    preprocessing[i][j] = min(preprocessing[i][j - 1], self.array[j])
        # pure lazyness :)
        self.preprocessing = preprocessing

    # O(1)
    def answerCompleteProceprocessingQuery(self, i, j):
        self.initCompletePreprocessing()
        return self.preprocessing[i][j]

    # we construct n / k intervals. Each interval has length k 
    # we calculate the min for each of the k intervals and store it
    def doLogPreprocessing(self):
        n = len(self.array)
        k = round(math.sqrt(n)) # seems k is log(n)
        count_segments = n // k if n % k == 0 else (n // k) + 1 # or (n - 1) // k + 1
        # will hold the min of the intervals
        self.logPreprocessing = [math.inf] *  ( count_segments ) 
        for index, element in enumerate(self.array):
            preprocessIndex = index // k
            self.logPreprocessing[preprocessIndex] = min(self.logPreprocessing[preprocessIndex], element)

    # O(k) complexity
    def answerLogPreprocesingQuery(self, i, j):
        self.initLogPreprocessing()
        k = round(math.sqrt(len(self.array)))

        minim = math.inf
        while i <= j:
            if i % k == 0 and i + k <= j:
                minim = min(minim, self.logPreprocessing[i // k])
                i += k
            else:
                minim = min(minim, self.array[i])
                i += 1

        return minim
    
    # sparseTable[i][j] - index of the minimum element starting at i of length 2**j
    def doSparseTableInitialize(self):
        n = len(self.array)
        k = int(math.log2(n)) + 1
        self.sparseTable = [ [ math.inf for _ in range(k)] for _ in range(n)]
        # init array
        for i in range(n):
            self.sparseTable[i][0] = i
        # calculate DP
        for j in range(1, k):
            for i in range( n + 1 - (1 << j) ): # M[i][j] covers i to (i + 2**j - 1) indexes, so i + 2 ** j - 1 <= n - 1 
                leftIndex = self.sparseTable[i][j - 1]
                rightIndex = self.sparseTable[i + (1 << (j - 1))][j - 1]
                
                self.sparseTable[i][j] = leftIndex if self.array[leftIndex] < self.array[rightIndex] else rightIndex
            
    # TODO - min and max range check (actually this is for the other solutions also)
    def answerSparseTableQuery(self, i, j):
        self.initSparseTablePreprocessing()
        
        k = int(math.log2(j - i + 1))
        
        leftValue = self.array[self.sparseTable[i][k]]
        rightValue = self.array[self.sparseTable[j - (1 << k) + 1][k]] 

        return leftValue if  leftValue < rightValue else rightValue

def test():
    array = [0, 1,2,3,4,5,6,7,8]

    rangeMinQuery = RangeMinimumQuery(array)
    
    assert (rangeMinQuery.answerCompleteProceprocessingQuery(0,2) == 0)
    assert (rangeMinQuery.answerCompleteProceprocessingQuery(3,6) == 3)
    assert (rangeMinQuery.answerCompleteProceprocessingQuery(2,2) == 2)
    assert (rangeMinQuery.answerCompleteProceprocessingQuery(4,5) == 4)
    assert (rangeMinQuery.answerCompleteProceprocessingQuery(1,7) == 1)
    
    
    assert (rangeMinQuery.answerLogPreprocesingQuery(0, 2) == 0)
    assert (rangeMinQuery.answerLogPreprocesingQuery(3, 6) == 3)
    assert (rangeMinQuery.answerLogPreprocesingQuery(2, 2) == 2)
    assert (rangeMinQuery.answerLogPreprocesingQuery(4, 5) == 4)
    assert (rangeMinQuery.answerLogPreprocesingQuery(1, 7) == 1)
    
    assert (rangeMinQuery.answerSparseTableQuery(0, 2) == 0)
    assert (rangeMinQuery.answerSparseTableQuery(3, 6) == 3)
    assert (rangeMinQuery.answerSparseTableQuery(2, 2) == 2)
    assert (rangeMinQuery.answerSparseTableQuery(4, 5) == 4)
    assert (rangeMinQuery.answerSparseTableQuery(5, 8) == 5)
    

test()


