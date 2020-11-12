"""

"""

class Solution():
    def __init__(self, array):
        self.array = array
    
    def findCandidateElement(self):
        candidate, count = self.array[0], 1

        for i in range(1, len(self.array)):
            current = self.array[i]
            if current == candidate:
                count += 1
            else:
                if count == 0:
                    count = 1
                    candidate = current
                else:
                    count -= 1
        return candidate

    def findMajoritaryElement(self):
        candidate = self.findCandidateElement()
        count = 0
        for elem in self.array:
            if candidate == elem:
                count += 1
        if 2 * count > len(self.array):
            return candidate
        else:
            return None

def test():
    s = [1,2,3,4,5,6,7]
    sol = Solution(s)
    elem = sol.findMajoritaryElement()
    assert (elem == None)
    s = [1,2,3,4,5,1,1,1, 1]
    sol = Solution(s)
    elem = sol.findMajoritaryElement()
    assert( elem == 1)

test()

        