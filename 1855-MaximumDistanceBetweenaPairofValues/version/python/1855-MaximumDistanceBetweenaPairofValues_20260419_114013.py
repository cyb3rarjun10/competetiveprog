# Last updated: 4/19/2026, 11:40:13 AM
1class Solution:
2    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
3
4        def binsearch(arr,l,r,target):
5            while l<r:
6                mid=l+(r-l)//2
7                if arr[mid]>=target:
8                    l=mid+1
9                else:
10                    r=mid
11            return l-1
12
13        maxdist=float('-inf')
14        for i in range(len(nums1)):
15            if nums1[i]>nums2[0]:
16                continue
17            x=binsearch(nums2,0,len(nums2),nums1[i])
18            if i>x:
19                continue
20            maxdist=max(maxdist,abs(x-i))
21        return maxdist if maxdist!=float('-inf') else 0
22
23
24
25        