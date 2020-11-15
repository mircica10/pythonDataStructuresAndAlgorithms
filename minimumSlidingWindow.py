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

class MinSlidingWindow():
    def __init__(self, arr, k):
        self.k = k
        self.arr = arr
        self.mapArrayToHeap = []
        self.mapHeapToArray = []

    def solve(self):
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
    tentative = sol.solve()
    assert(answer == tentative)

    arr = [0,1,2,3,4]
    k = 2
    answer = [0, 0, 1, 2, 3]
    sol = MinSlidingWindow(arr, k)
    tentative = sol.solve()
    assert(answer == tentative)

test()