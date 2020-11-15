"""
Se dă un vector. Să se găsească min(v[i], v[i + 1], ..., v[i + k - 1]) pentru
 fiecare i = 0, 1, ..., n - k.

Există o soluție în O(n) amortizat care folosește un deque (o coadă cu două capete). 
Găsiți implementarea în media:msw.cpp.

La nevoie, soluția cu heap este mai simplu de găsit și merge în O(n log k). 
Totuși, ștergerea din heap (în clipa în care un element iese din fereastră) nu este banală. 
Pentru a putea face ștergeri, avem nevoie să reținem un vector suplimentar cu poziția 
fiecărui element în heap. Când două elemente sunt interschimbate în heap, și pozițiile lor 
trebuie interschimbate în vector.

"""

from heapImplementation import Heap
from collections import deque

class MinSlidingWindow():
    def __init__(self, arr, k):
        self.k = k
        self.arr = arr
        self.mapArrayToHeap = []
        self.mapHeapToArray = []


    def solveWithDeque(self):
        minimums = []
        coada = deque()
        for index, current_element in enumerate(self.arr):
            # we discard the elements bogger than the current one, as they will never be minimum after
            while len(coada) > 0:
                stack_peek = coada[-1]
                if stack_peek[1] > current_element:
                    coada.pop()
                else:
                     break
            # add tuple current element AND its index
            coada.append((index, current_element))
            
            # we discard the elements with the index not in the window
            left_margin = index - self.k
            while len(coada) > 0 and left_margin >= 0:
                queue_peek = coada[0]
                if queue_peek[0] <= left_margin:
                    coada.popleft()
                else:
                    break
            # minimum is the first element
            minimums.append(coada[0][1])
        return minimums    


    def solveWithHeap(self):
        minimus = []
        heap = Heap()
        for index, element in enumerate(self.arr):
            heap.minInsert(element)
            if index >= self.k:
                #we need to remove an element from the heap, as the window slides
                indexToRemove = index - self.k
                indexToRemoveInHeap = heap.mapArrayToHeap[indexToRemove]
                heap.minDelete(indexToRemoveInHeap)
            minimus.append(heap.minimum())
        return minimus


def test():
    arr = [0,1,2,3,4,5,6]
    k = 3
    answer = [0,0,0,1, 2,3,4]
    sol = MinSlidingWindow(arr, k)
    tentative = sol.solveWithHeap()
    assert(answer == tentative)

    arr = [0,1,2,3,4]
    k = 2
    answer = [0, 0, 1, 2, 3]
    sol = MinSlidingWindow(arr, k)
    tentative = sol.solveWithHeap()
    assert(answer == tentative)

    arr = [0,1,2,3,4,5,6]
    k = 3
    answer = [0,0,0,1, 2,3,4]
    sol = MinSlidingWindow(arr, k)
    tentative = sol.solveWithDeque()
    assert(answer == tentative)

    arr = [0,1,2,3,4]
    k = 2
    answer = [0, 0, 1, 2, 3]
    sol = MinSlidingWindow(arr, k)
    tentative = sol.solveWithDeque()
    assert(answer == tentative)



test()