# Last updated: 4/19/2026, 11:58:32 AM
1class Solution:
2    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
3        maxdist=float('-inf')
4        j=0
5        for i in range(len(nums1)):
6            if nums1[i]>nums2[0]:
7                continue
8            while j<len(nums2) and nums2[j]>=nums1[i]:
9                j+=1
10            if i>j:
11                break
12            maxdist=max(maxdist,abs(j-i-1))
13        return maxdist if maxdist!=float('-inf') else 0
14
15
16        