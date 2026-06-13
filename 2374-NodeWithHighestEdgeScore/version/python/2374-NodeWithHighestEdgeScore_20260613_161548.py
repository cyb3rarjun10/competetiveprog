# Last updated: 6/13/2026, 4:15:48 PM
1class Solution:
2    def edgeScore(self, edges: List[int]) -> int:
3        d=defaultdict(int)
4        for i in range(len(edges)):
5            d[edges[i]]+=i
6        maxval=float('-inf')
7        maxnode=0
8        for key,value in sorted(d.items(), key=lambda item:(item[0])):
9            if value>maxval:
10                maxval=value
11                maxnode=key
12        return maxnode