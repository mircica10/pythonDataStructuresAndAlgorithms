class Solution:
    def __init__(self, array):
        self.array = array
    
        """
        // invariant: la fiecare moment,
  // * s[lo ... left - 1] conține elemente unde al pos-lea caracter este mai mic decât mid
  // * s[left ... curr - 1] conține elemente unde al pos-lea caracter este egal cu mid
  // * s[curr] este șirul curent, din care evaluăm al pos-lea caracter
  // * s[curr + 1 ... right] conține elemente încă neevaluate
  // * s[right + 1 ... hi] conține elemente unde al pos-lea caracter este mai mare decât mid
         """
    def solve(self, low, high, position):
        if low >= high:
            return
        curr = low
        left, right = low, high
        mid = chr( ( ord( self.array[low][position]) + ord( self.array[high][position]) ) // 2)
        while curr <= right:
            c = self.array[curr][position]
            if c < mid:
                self.array[curr], self.array[left] = self.array[left], self.array[curr]
                curr += 1
                left += 1
            elif c > mid:
                self.array[curr], self.array[right] = self.array[right], self.array[curr]
                right -= 1
            else:
                curr += 1

        self.solve(low, left - 1, position)
        if position < len(self.array[left]):
            self.solve(left, right, position + 1)
        self.solve(right + 1, high, position)


    def helper(self):
        n = len(self.array)
        self.solve(0, n - 1, 0)
        return self.array

def test():
    sir = ["asc", "dfd", "tzh", "sea", "adj", "dfa"]
    sol = Solution(sir)
    sorted_sir = sol.helper()
    assert(sorted_sir == ['adj', 'asc', 'dfa', 'dfd', 'sea', 'tzh'])

test()