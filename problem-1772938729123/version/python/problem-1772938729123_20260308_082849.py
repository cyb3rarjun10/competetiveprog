# Last updated: 3/8/2026, 8:28:49 AM
1class Solution:
2    def smallestBalancedIndex(self, nums: list[int]) -> int:
3        ts=sum(nums)
4        rs=0
5        rp=1
6        idx=-1
7        mv=sum(abs(x) for x in nums) +1
8        for i in range(len(nums)-1,-1,-1):
9            ls=ts-rs-nums[i]
10            if ls==rp:
11                idx=i
12            rs+=nums[i]
13            rp*=nums[i]
14            if rp>mv:
15                rp=mv
16            elif rp<-mv:
17                rp=-mv
18        return idx
19            
20            