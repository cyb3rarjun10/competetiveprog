# Last updated: 4/5/2026, 8:43:08 AM
1class Solution:
2    def findGoodIntegers(self, n: int) -> list[int]:
3        cubes=[]
4        i=1
5        while i**3 <=n:
6            cubes.append(i**3)
7            i+=1
8        d=defaultdict(int)
9        m=len(cubes)
10        for i in range(m):
11            j=m-1
12            while j>=i:
13                s=cubes[i]+cubes[j]
14                if s>n:
15                    j-=1
16                else:
17                    d[s]+=1
18                    j-=1
19        return sorted([x for x,c in d.items() if c>1])