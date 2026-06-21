# Last updated: 6/21/2026, 8:14:55 AM
1class Solution:
2    def maxDistance(self, moves: str) -> int:
3        d=Counter(moves)
4        n=len(moves)
5        spacemove=""
6        noofleft=d['L']
7        noofright=d['R']
8        noofup=d['U']
9        noofdown=d['D']
10        
11        #decide to move right or left or up or down on _
12        xd=abs(noofleft-noofright)
13        yd=abs(noofup-noofdown)
14
15        if xd>yd:
16            if noofleft>noofright:
17                spacemove='L'
18            else:
19                spacemove='R'
20        else:
21            if noofup>noofdown:
22                spacemove='U'
23            else:
24                spacemove='D'
25        
26        x=0
27        y=0
28        for i in range(n):
29            if moves[i]=='U':
30                x-=1
31            elif moves[i]=='D':
32                x+=1
33            elif moves[i]=='L':
34                y-=1
35            elif moves[i]=='R':
36                y+=1
37            else:
38                if spacemove=='D':
39                    x+=1
40                elif spacemove=='U':
41                    x-=1
42                elif spacemove=='L':
43                    y-=1
44                else:
45                    y+=1
46        return abs(0-x)+abs(0-y)
47