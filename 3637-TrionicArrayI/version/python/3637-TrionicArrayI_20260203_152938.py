# Last updated: 2/3/2026, 3:29:38 PM
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        i=0
4        n=len(nums)
5        while i<n-1 and nums[i+1]>nums[i]:
6            i+=1
7        if(i==0):
8            return False
9        j=i
10        while j<n-1 and nums[j+1]<nums[j]:
11            j+=1
12        if j==i:
13            return False
14        k=j
15        while k<n-1 and nums[k+1]>nums[k]:
16            k+=1
17        if k==j:
18            return False
19
20        return k==n-1