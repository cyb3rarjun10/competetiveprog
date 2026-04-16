# Last updated: 4/16/2026, 4:52:33 PM
1class Solution:
2    def isRobotBounded(self, instructions: str) -> bool:
3        #0=north,90=east,180=south,270=west
4        curr=0
5        x=0
6        y=0
7        print(x,y,curr)
8        for i in instructions:
9            if i=='L':
10                curr=(curr-90 + 360)%360
11            elif i=='R':
12                curr=(curr+90)%360
13            else:
14                if curr==0:
15                    y+=1
16                elif curr==90:
17                    x+=1
18                elif curr==180:
19                    y-=1
20                else:
21                    x-=1
22            print(x,y,curr)
23        if x==0 and y==0:
24            return True
25        if curr==0:
26            return False
27        return True
28        
29
30
31