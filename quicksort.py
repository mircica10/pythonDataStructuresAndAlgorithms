class Quicksort():
    def __init__(self, arr):
        self.arr = arr
    
    def quickHoare(self, i, j):
        if i < j:
            middle = self.partitionHoare(i, j)
            self.quickHoare(i, middle)
            self.quickHoare(middle + 1, j)
    
    def partitionHoare(self, start, end):
        middle = start + (end - start) // 2
        pivot = self.arr[middle]
        i = start - 1
        j = end + 1

        while True:
            while True:
                i += 1
                if self.arr[i] >= pivot:
                    break
            while True:
                j -= 1
                if self.arr[j] <= pivot:
                    break            
            if i >= j:
                return j
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
      
    def quickLamuto(self, i, j):
        if i < j:
            p = self.partitionLamuto(i, j)    
            self.quickLamuto(i, p - 1)
            self.quickLamuto(p + 1, j)

    def partitionLamuto(self, start, end):
        pivot = self.arr[end]
        i = start
        for j in range(start, end):
            if self.arr[j] < pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[end] = self.arr[end], self.arr[i]
                
        return i

def test():
    arr = [1,3,4,2,5,76,4,32,434]
    q = Quicksort(arr)
    q.quickHoare(0, len(arr) - 1)
    for i in range(1, len(arr)):
        assert(arr[i - 1] <= arr[i])

    arr = [1,3,4,2,5,76,4,32,434]
    q = Quicksort(arr)
    q.quickLamuto(0, len(arr) - 1)
    for i in range(1, len(arr)):
        assert(arr[i - 1] <= arr[i])
    

test()