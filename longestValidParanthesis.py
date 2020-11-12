"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.
"""

from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.solveStack(s)

    def solveTLE(self, s):
        self.max = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if self.isCorrect(s[i:j + 1]):
                    self.max = max(self.max, j - i + 1)
        return self.max


    def isCorrect(self, s):
        stack = []
        for elem in s:
            if  elem == '(':
                stack.append('(')
            if elem == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False 
        return len(stack) == 0

    def solveStack(self, s):
        global_max = 0
        stack = []
        stack.append(-1)
        for index, elem in enumerate(s):
            if elem == '(':
                stack.append(index)
            elif elem == ')':
                stack.pop()
                if len(stack) == 0:
                    stack.append(index)
                else:
                    local_max = index - stack[len(stack) - 1]
                    global_max = max(global_max, local_max)
        return global_max



def test():
    sol = Solution()
    s = "(()"
    correct_answer = 2
    answer = sol.longestValidParentheses(s)
    assert(answer == correct_answer)

    s = ")()())"
    correct_answer = 4
    answer = sol.longestValidParentheses(s)
    assert(answer == correct_answer)

    s = "()(()"
    correct_answer = 2
    answer = sol.longestValidParentheses(s)
    assert(answer == correct_answer)

test()