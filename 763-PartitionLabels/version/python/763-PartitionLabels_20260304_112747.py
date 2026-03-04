# Last updated: 3/4/2026, 11:27:47 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        n=len(s)
4        """d={}
5        for i in range(len(s)-1,-1,-1):
6            if s[i] not in d:
7                d[s[i]]=i"""
8        farthest=0
9        partitions=[]
10        left=0
11        for i in range(n):
12            farthest=max(farthest,s.rfind(s[i]))
13            if i==farthest:
14                partitions.append(i+1 -left)
15                left=i+1
16        return partitions
17
18