# Last updated: 3/16/2026, 11:05:08 PM
1class Solution:
2    def minOperations(self, nums: List[int]) -> int:
3        def swap(i):
4            if nums[i]==1:
5                nums[i]=0
6            else:
7                nums[i]=1
8                
9        n=len(nums)
10        c=0
11        for i in range(n-2):
12            if nums[i]==0:
13                c+=1
14                swap(i)
15                swap(i+1)
16                swap(i+2)
17        if nums[-1]==nums[-2]==1:
18            return c
19        return -1
20        
21