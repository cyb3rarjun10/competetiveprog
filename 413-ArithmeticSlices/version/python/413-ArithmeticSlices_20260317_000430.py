# Last updated: 3/17/2026, 12:04:30 AM
1class Solution:
2    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n<3:
5            return 0
6        res=0
7        l=0
8        diff=nums[1]-nums[l]
9        for r in range(2,n):
10            if nums[r]-nums[r-1]!=diff:
11                diff=nums[r]-nums[r-1]
12                l=r-1
13            if r-l +1>=3:
14                res+=(r-l+1)-2
15            
16        return res
17
18                
19            
20            
21            
22
23
24
25