# Last updated: 3/29/2026, 8:51:54 AM
1class Solution:
2    def sortableIntegers(self, nums: list[int]) -> int:
3        n=len(nums)
4        klist=[i for i in range(1,n//2 +1) if n%i==0] + [n]
5        target=sorted(nums)
6        res=0
7        for k in klist:
8            valid=True
9            for i in range(0,n,k):
10                a=nums[i:i+k]
11                b=target[i:i+k]
12                d=0
13                di=-1
14                for idx in range(1,k):
15                    if a[idx-1]>a[idx]:
16                        d+=1
17                        di=idx-1
18                    if d>1:
19                        break
20                if d>1:
21                    valid=False
22                    break
23                elif d==0:
24                    if a!=b:
25                        valid=False
26                        break
27                else:
28                    if a[di+1:]+a[:di+1] !=b:
29                        valid=False
30                        break
31            if valid:
32                res+=k
33        return res
34                
35                