class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
                
        subarray[i] - index % numrows == i or index % numrows == numrows - i 
                
        """
        return self.aproach1(s, numRows)

    def aproach3(self, s, numRows):
        if numRows == 1 or len(s) < numRows:
            return s
        
        cycle = 2 * numRows - 2
        res = []

        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res.append(s[j])
                k = j + cycle - 2 * i
                if i != 0 and i != numRows - 1 and k < len(s):
                    res.append(s[k])

        return ''.join(res)



    def aproach1(self, s, numRows):
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        buckets = [[] for _ in range(numRows)]
        counter = 0
        direction = -1
     
        for i in range(len(s)):
            buckets[counter].append(s[i])
            if counter == numRows - 1 or counter == 0:
                direction *= -1
            counter += direction
            
        final = []
        for bucket in buckets:
            final.extend(bucket)
        
        return ''.join(final)
        

    def aproach2(self, s, numRows):
        #init variables
        lines = [[] for _ in range(numRows)]
        #cycle represents a complete zigzag (e.g for numRows 3 value is 4, for 4 is 6 and so on)
        cycle = numRows if numRows < 3 else 2 + (numRows - 2) * 2
        
        
        for i in range(len(s)):
            #cycle_index is the index in a complete zigzag
            cycleIndex = i % cycle
            #line_number is the index of the line in a zigzag movement 
            lineNumber = cycleIndex if cycleIndex < numRows else (2 * (numRows - 1) - cycleIndex)
            #we add the character to its line
            lines[lineNumber].extend(s[i])
            
        #union of all the lines
        answer = []
        for line in lines:
            answer.extend(line)
        
        return ''.join(answer)
        

def test():
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    s2 = sol.convert(s, numRows)
    assert(s2 == "PAHNAPLSIIGYIR")

test()