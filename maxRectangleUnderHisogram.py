
class MaxRectangleHistogram():
    def __init__(self, heights):
        self.heights = heights 
        self.heights = [0] + self.heights + [0] # sentinels to force stack empty

    def getMaxArea(self):
        stack = []
        max_area = 0

        for index, height in enumerate(self.heights):
            right_index = stack[len(stack) - 1][0] if len(stack) > 0 else None

            while len(stack) > 0 and stack[len(stack) - 1][1] > height:
                _ , stack_top_val = stack.pop() 

                left_index = 0 if len(stack) == 0 else stack[len(stack) - 1][0]
                    
                curr_area = stack_top_val * (right_index - left_index)
                max_area = max(max_area, curr_area)
            stack.append((index, height))            
            
        return max_area

# TODO - stack with a simple array and an index

def test():
    heights = [6, 2, 5, 4, 5, 1, 6]
    maxRect = MaxRectangleHistogram(heights)
    answer = 12
    tentative = maxRect.getMaxArea()

    assert(answer == tentative)

    heights = [6, 2, 5, 4, 4, 5, 1, 6]
    maxRect = MaxRectangleHistogram(heights)
    answer = 16
    tentative = maxRect.getMaxArea()
    assert(answer == tentative)

    heights = [2, 3]
    maxRect = MaxRectangleHistogram(heights)
    answer = 4
    tentative = maxRect.getMaxArea()
    assert(answer == tentative)

test()