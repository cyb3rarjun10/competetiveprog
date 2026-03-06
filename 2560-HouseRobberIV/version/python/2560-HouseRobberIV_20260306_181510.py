# Last updated: 3/6/2026, 6:15:10 PM
1class Solution:
2    def minCapability(self, nums: List[int], k: int) -> int:
3        n=len(nums)
4        l=1 #minreward
5        r=max(nums) #maxreward
6        while l<r:
7            mid=(l+r)//2
8            idx=0
9            houserobbed=0
10            while idx<n:
11                if nums[idx]<=mid:
12                    houserobbed+=1
13                    idx+=2
14                else:
15                    idx+=1
16            if houserobbed>=k:
17                r=mid
18            else:
19                l=mid+1
20        return l
21
22