"""
http://campion.edu.ro/arhiva/index.php?page=problem&action=view&id=1584
"""

class Triunghi6():
    def __init__(self, array):
        self.array = array

    # this is the array with the min  element as the init element
    def constructMinArray(self, k):
        arr = [None for _ in range(k)]
        firstElement = min(self.array)
        arr[0] = arr[1] = firstElement
        counter = 2
        while counter < k:
            arr[counter] = arr[counter - 1] + arr[counter - 2]
            counter += 1
        return arr

    def constructMinArrayAllNumbersIncluded(self, k):
        pointerInitialArray = 0
        arr = [1, 1]
        # we sort the array
        self.array.sort()
        # dummy case, initial array contains a pair (this will be the first two elements) 
        # we adjunst the point pointer and modifiy the elements of the returned array
        if self.array[0] == self.array[1]:
            arr = [self.array[0], self.array[1]]
            pointerInitialArray = 2
        
        # make sure all the element of initial array are in the new array
        while pointerInitialArray < len(self.array):
            k1 = len(arr)
            elem1, elem2 = arr[k1 - 1] , arr[k1 - 1] + arr[k1 - 2]
            if elem1 + elem2 >= self.array[pointerInitialArray]:
                arr.append(self.array[pointerInitialArray])
                pointerInitialArray += 1
            else:
                arr.append(elem2)
                

        # make sure the new array has the requested k length
        counter = len(arr)
        while counter < k:
            arr.append(arr[counter - 1] + arr[counter - 2])
            counter = len(arr)

        return arr

        
def test():
    arr = [1,1,4,9,16]
    sol = Triunghi6(arr)
    minArr = sol.constructMinArray(10)
    testNotTriangle(minArr)
    minArrAllElems = sol.constructMinArrayAllNumbersIncluded(12)
    testNotTriangle(minArrAllElems)

def testNotTriangle(arr):
    for i in range(2, len(arr)):
        assert (arr[i - 2] + arr[i - 1] <= arr[i]) 
    

test()


     
        
