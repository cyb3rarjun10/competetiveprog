# Last updated: 6/14/2026, 8:36:59 AM
1class Solution:
2    def maxRatings(self, units: List[List[int]]) -> int:
3        row=len(units)
4        col=len(units[0])
5
6        if col==1:
7            return sum(units[i][0] for i in range(row))
8
9        trashmin=float('inf')
10        trashm2=float('inf')
11        sumofall=0
12
13        for d in units:
14            min1=float('inf')
15            min2=float('inf')
16            for u in d:
17                if u<min1:
18                    min2=min1
19                    min1=u
20                elif u<min2:
21                    min2=u
22            if trashmin>min1:
23                trashmin=min1
24            if trashm2>min2:
25                trashm2=min2
26            sumofall+= min2
27
28        return trashmin + sumofall- trashm2
29                
30                
31                