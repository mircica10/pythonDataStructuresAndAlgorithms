"""
"""

class bitImplementation:
    def __init__(self, arr):
        self.arr = arr
        self.bit = [0] * (len(self.arr) + 1)
        self.initBit()

    def initBit(self):
        for i in range(1, len(self.bit)):
            # get smallest power on 2 for "i" representation
            m = i & (-i)
            s = 0
            for j in range(i - m, i):
                s += self.arr[j]
            self.bit[i] = s 

    def sum(self, index):
        s = 0
        while index:
            s += self.bit[index]
            index &= (index - 1)
        return s
    
    def add(self, val, index):
        while True:
            self.bit[index] += val
            index += (index & (-index))
            if index >= len(self.bit):
                break

    # get single value in O(1) -  great idea
    def val(self, index):
        s = self.bit[index]
        parent = index & (index - 1)
        while index != parent:
            s -= self.bit[index]
            index &= (index - 1)
        return s

    # greatest val for which sum(1, x) < val
    def searchPartialSum(self, val):
        index = 0
        interval = len(self.bit) // 2
        while interval:
            if self.bit[index + interval] < val:
                val -= self.bit[index + interval]
                index += interval
            interval >>= 1
        return index


def test():
    arr = [2,5,1,0,4,8]
    bit = bitImplementation(arr)
    assert( bit.bit == [0, 2, 7, 1, 8, 4, 12])

test()