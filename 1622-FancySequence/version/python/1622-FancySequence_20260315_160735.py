# Last updated: 3/15/2026, 4:07:35 PM
1class Fancy:
2    def __init__(self):
3        self.mod = 10**9 + 7  
4        self.val = []  
5        self.a = 1  
6        self.b = 0  
7
8    def append(self, val: int) -> None:
9        x = (val - self.b + self.mod) % self.mod
10        self.val.append(x * pow(self.a, self.mod - 2, self.mod) % self.mod)
11
12    def addAll(self, inc: int) -> None:
13        self.b = (self.b + inc) % self.mod
14
15    def multAll(self, m: int) -> None:
16        self.a = (self.a * m) % self.mod
17        self.b = (self.b * m) % self.mod
18
19    def getIndex(self, idx: int) -> int:
20        if idx >= len(self.val):
21            return -1  
22        return (self.a * self.val[idx] + self.b) % self.mod
23
24
25# Your Fancy object will be instantiated and called as such:
26# obj = Fancy()
27# obj.append(val)
28# obj.addAll(inc)
29# obj.multAll(m)
30# param_4 = obj.getIndex(idx)