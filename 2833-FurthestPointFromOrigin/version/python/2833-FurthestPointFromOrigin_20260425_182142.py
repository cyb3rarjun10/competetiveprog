# Last updated: 4/25/2026, 6:21:42 PM
1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        u,r,l=0,0,0
4        for i in moves:
5            if i=="_":
6                u+=1
7            elif i=="R":
8                r+=1
9            else:
10                l+=1
11        
12        return (max(l,r)+u)-min(l,r)