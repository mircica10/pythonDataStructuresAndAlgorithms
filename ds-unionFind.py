from typing import List

class UnionFind:
    def _init_(self, v: List[int]):
        # v[i] = j - j ist the set number of element 1
        self.v = v
        # size[i] - number of elements in the set of i
        # just for the exponent of the set is the number set, for the others is None
        self.size = []
        # link the other elements in a set
        self.next = []
    
    def init(self):
        for i in len(self.v):
            self.v[i] = i
            self.size = 1
            self.next = i
    
    def find(self, i: int) -> int:
        return self.v[i]

    def union(self, x: int, y: int):
        fx = self.find(x)
        if fx != self.find(y):
            self.size[x] += self.size[y]
            i = y
            # we change all y to x set
            while True:
                self.v[i] = fx
                i = self.next[i]
                if i == y:
                    break
            # we connect the 2 linked lists to form one list only
            nx = self.next[x]
            self.next[x] = self.next[y] 
            self.next[y] = nx
    



"""
void init(int n) {
    for (int i = 0; i < n; i++) {
      p[i] = i;
    }
  }

  void union(int x, int y) {
    int rx = find(x), ry = find(y);
    if (rx != ry) {
      p[rx] = ry;    // unim rădăcinile între ele
    }
  }

  int find(int x) {
    while (p[x] != x) {
      x = p[x];
    }
    return x;
  }
"""


class UnionFind2:
    def _init_(self, n):
        self.p = [] * n 
    
    def init(self):
        for i in range(len(p)):
            self.p[i] = i

    def find(self, x):
        while p[x] != x:
            x = p[x]
        return x

    def union(x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            p[rx] = ry


class UnionFind3:
    def _init_(self, n):
        self.p = [] * n 
        self.h = [] * n
    
    def init(self):
        for i in range(len(p)):
            self.p[i] = i
            self.h[i] = 1

    def find(self, x):
        r = x
        while p[r] != r:
            r = p[r]
        # we modify the elements on the way to make the path smaller
        while p[x] != r:
            temp = p[x]
            p[x] = r
            x = temp        
        return r

    def union(x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if h[rx] < h[ry]:
                p[rx] = ry
            elif h[rx] > h[ry]:
                p[ry] = rx
            else:
                p[rx] = ry
                h[rx] += 1 

