# Last updated: 6/21/2026, 8:24:43 AM
1class Solution:
2    def countValidSubarrays(self, nums: list[int], x: int) -> int:
3        x=str(x)
4        n=len(nums)
5        pref=[0]
6        presum=0
7        for i in range(n):
8            presum+=nums[i]
9            pref.append(presum)
10        res=0
11        for i in range(n):
12            for j in range(i+1,n+1):
13                temp=pref[j]-pref[i]
14                temp=str(temp)
15                if temp[0]==x and temp[-1]==x:
16                    res+=1
17        return res
18
19                