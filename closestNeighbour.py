"""
Să considerăm problema celui mai apropiat vecin: 
Dându-se un vector V, să se calculeze un alt vector W unde W(i) este cel mai mare indice j < i 
pentru care V[j] < V[i]. 
Când nu există un astfel de j, atunci V[i] = 0. 
"""

from math import inf

class Solution():
    def solve(self, v):
        v = [-inf] + v # sentinel
        w = [0] * len(v)
        n = len(v)
        stack = [0] # sentinel
        for idx in range(1, n):
            while v[idx] < v[stack[len(stack) - 1]]:
                stack.pop()
            w[idx] = stack[len(stack) - 1]
            stack.append(idx)
        # adjust the indexes to 
        w = [i - 1 if i != 0 else i for i in w]
        return w[1:]

def test():
    v = [5,3,4,6,7,8,6,4]
    w = Solution().solve(v)
    print(w)
    #correct = [0, 0, 0, 3, 4, 6, 7, 6, 4]
    #assert(w == correct)


test()

            