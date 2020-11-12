"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
You can return the answer in any order.

Example:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
"""
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        i = 0
        #construct hash
        hash = self.getHash(words)
        len_word = len(words[0])
        while i + len_word <= len(s):
            if s[i:i + len_word] in hash:
                isSolution = self.testSubarray(i, s, words)
                if isSolution:
                    res.append(i)
            i += 1
        return res

    def testSubarray(self, start, s, words):
        len_word = len(words[0])
        words_count = len(words)
        hash = self.getHash(words)
        counter = 0
        while counter < words_count:
            candidate = s[start + counter * len_word : start + (counter + 1) * len_word]
            if not (candidate in hash):
                return False
            if candidate in hash and hash[candidate] <= 0:
                return False
            hash[candidate] -= 1
            counter += 1
        return True     



    def getHash(self, words):
        hash = {}
        for word in words:
            if word in hash:
                hash[word] = hash[word] + 1
            else:
                hash[word] = 1
        return hash    


def test():
    sol = Solution()
    
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    res1_correct = [0,9]
    res1 = sol.findSubstring(s, words)
    assert(res1 == res1_correct)
    
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    res1_correct = []
    res1 = sol.findSubstring(s, words)
    assert(res1 == res1_correct)

    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    res1_correct = [6, 9, 12]
    res1 = sol.findSubstring(s, words)
    assert(res1 == res1_correct)
    
    s = "a"
    words = ["a"]
    res1_correct = [0]
    res1 = sol.findSubstring(s, words)
    assert(res1 == res1_correct)
    

test()