
class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        
        
        TODO


        """
        
        hasDigit = hasUppercase = hasLowercase = 1
        missing_specials = 0

        for character in s:
            if character >= 'a' and character <= 'z':
                hasLowercase = 0
            elif character >= 'A' and character <= 'Z':
                hasUppercase = 0
            elif character >= '0' and character <= '9':
                hasDigit = 0
        
        missing_specials = hasDigit + hasLowercase + hasUppercase

        size = len(s)
        counter = 0
        one = 0# # groups of length 3k
        two = 0# # groups of length 3k + 1
        three = 0# # groups of length 3k + 2
        change = 0# # of groups of 3

        while counter < size:
            index = 1
            while counter + index < size and s[counter] == s[counter + index]:
                index += 1
            #update the number of changes
            change += index // 3
            #update the number of arrays
            if index >= 3: 
                if index % 3 == 0:
                    one += 1
                elif index % 3 == 1:
                    two += 1
                elif index % 3 == 2:
                    three += 1
            counter += index 
        
        #we have 3 cases, depending on size of the string
        # case 1
        if size < 6:
            if missing_specials < 6 - size:
                return 6 - size
            else:
                return missing_specials        
        #case 2
        if size >= 6 and size <= 20:
            return self.max(missing_specials, change)
        #case 3 -- this is the biggest. we need to cut size - 20 elements. 
        #       -- we will try to cut those from repeating arrays
        if size > 20:
            delete = size - 20
            #we cut from 3k length arrays
            change -= self.min(delete, one)
            change -= self.min(self.max(delete - one, 0), two * 2) // 2
            change -= self.max(delete - one - 2 * two, 0) // 3
        
        return delete + self.max(change, missing_specials) 

    def max(self, a, b):
        return a if a > b else b
    def min(self, a, b):
        return a if a < b else b

def test():
    sol = Solution()
    a = "1Abababcaaaabababababa"
    min = sol.strongPasswordChecker(a)
    print(min)

test()    
    