# Last updated: 6/2/2026, 9:30:05 AM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        m=len(waterStartTime)
4        n=len(landStartTime)
5        lrd=[]
6        for i in range(len(landStartTime)):
7            lrd.append(landStartTime[i]+landDuration[i])
8        wrd=[]
9        for i in range(len(waterStartTime)):
10            wrd.append(waterStartTime[i]+waterDuration[i])
11        x=min(lrd)
12        y=min(wrd)
13        minwf=999999
14        minlf=999999
15        for i in range(len(landStartTime)):
16            lf=landStartTime[i]+landDuration[i]
17            for j in range(m):
18                wst=max(lf,waterStartTime[j])
19                f=wst+waterDuration[j]
20                minlf=min(minlf,f)
21        for i in range(m):
22            wf=waterStartTime[i]+waterDuration[i]
23            for j in range(n):
24                lst=max(wf,landStartTime[j])
25                f=lst+landDuration[j]
26                minwf=min(minwf,f)
27        
28        return min(minlf,minwf)
29        
30
31        
32        