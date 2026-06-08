# Last updated: 6/8/2026, 4:10:31 PM
1class Solution:
2    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
3        stck=[(0,0)]
4        v=set()
5        while stck:
6            a,b=stck.pop()
7            if a+b ==target:
8                return True
9            if (a,b) in v:
10                continue
11            v.add((a,b))
12            #fill jug 1 
13            stck.append((x,b))
14            #fill jug 2
15            stck.append((a,y))
16            #empty jug 1
17            stck.append((0,b))
18            #empty jug 2
19            stck.append((a,0))
20
21            w = min(a, y - b)
22            stck.append((a - w, b + w))
23
24            w = min(b, x - a)
25            stck.append((a + w, b - w)) 
26
27        return False