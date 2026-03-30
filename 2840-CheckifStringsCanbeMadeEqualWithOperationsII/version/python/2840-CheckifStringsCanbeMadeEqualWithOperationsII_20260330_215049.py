# Last updated: 3/30/2026, 9:50:49 PM
1class Solution:
2    def checkStrings(self, s1: str, s2: str) -> bool:
3        s1odd=[]
4        s1eve=[]
5        s2odd=[]
6        s2eve=[]
7        for i in range(len(s1)):
8            if i%2==0:
9                s1eve.append(s1[i])
10                s2eve.append(s2[i])
11            else:
12                s1odd.append(s1[i])
13                s2odd.append(s2[i])
14        s1odd.sort()
15        s2odd.sort()
16        s1eve.sort()
17        s2eve.sort()
18        return s1odd==s2odd and s2eve==s1eve
19
20        