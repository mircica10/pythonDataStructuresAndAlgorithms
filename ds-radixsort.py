class Solution:
    def __init__(self, array):
        self.array = array
    """
    sort on the least significat bin
    craete another array in order and so on
    we assume all the numbers have the same number of digits
    ideas - this can be extended to other data type string and 
    """
    def solve(self):        
        sortedArray = self.array.copy()
        # we iterate for each digit
        no_iterations = len(str(self.array[0]))
        # we iteratate for  all digits, starting with the least significant one
        for i in range(no_iterations):
            # reset the bins
            bins = [[] for i in range(10)]
            # for each elements in array
            for element in sortedArray:
                # append the element to the corresponding bin 
                # e.g. second iteration for 543 is 4, first is 3 and so on
                bin_number = (element // pow(10, i)) % 10 
                bins[bin_number].append(element)
            # clear sorted array for the next iteration
            sortedArray = []
            # add elements from bin to array
            for curr_bin in bins:
                for item in curr_bin:
                    sortedArray.append(item)  
        # this will hold the sorted array after the last iteration, so return      
        return sortedArray    


def test():
    sir = [83, 13, 23, 55, 47, 18, 58, 19]
    sol = Solution(sir)
    sorted_sir = sol.solve()
    assert(sorted_sir == [13, 18, 19, 23, 47, 55, 58, 83])

test()
