
# this heap keeps track of the changes in the heap in respect to the initial array
# used to solve minimum sliding window problem

class Heap():
    def __init__(self):
        self.arr = [] # this holds the heap
        self.n = 0 # size of the heap
        self.mapArrayToHeap = [] # modified just for insert and heap stuff
        self.mapHeapToArray = [] # modified just for insert and heap stuff

    def left(self, i):
        return 2 * i
    
    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return i // 2

    def minHeapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i
        if left < self.n and self.arr[i] > self.arr[left]:
            smallest = left
        if right < self.n and self.arr[smallest] > self.arr[right]:
            smallest = right
        if smallest != i:
            self.swap(i,smallest)        
            self.minHeapify(smallest)

    def appendElem(self, value):
        self.n = self.n + 1
        self.arr.append(value)
        # an inserted elem will be append at the back of the heap
        self.mapArrayToHeap.append(self.n - 1)
        # back of the heap contains pointer to size of mapArrayToHeap
        self.mapHeapToArray.append(len(self.mapArrayToHeap) - 1)
       
    def minInsert(self, value):
        self.appendElem(value)
        i = self.n - 1
        while i > 0 and self.arr[i] < self.arr[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)


    def minDelete(self, i):
        self.swap(i, self.n - 1)
        self.n = self.n - 1
        self.arr = self.arr[:self.n]
        self.minHeapify(i)

    def minimum(self):
        assert(self.n > 0)
        return self.arr[0]

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.mapArrayToHeap[self.mapHeapToArray[i]], self.mapArrayToHeap[self.mapHeapToArray[j]] = self.mapArrayToHeap[self.mapHeapToArray[j]], self.mapArrayToHeap[self.mapHeapToArray[i]]
        self.mapHeapToArray[i], self.mapHeapToArray[j] = self.mapHeapToArray[j], self.mapHeapToArray[i]
        

def testHeap():    
    heap = Heap()
    heap.minInsert(3)
    assert(3 == heap.minimum())
    heap.minInsert(8)
    assert(3 == heap.minimum())
    heap.minInsert(2)
    assert(2 == heap.minimum())
    heap.minInsert(9)    
    assert(2 == heap.minimum())
    heap.minInsert(1)
    assert(1 == heap.minimum())
    heap.minDelete(0)
    assert(2 == heap.minimum())
testHeap()
    


