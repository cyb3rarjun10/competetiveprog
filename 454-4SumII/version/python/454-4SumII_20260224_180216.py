# Last updated: 2/24/2026, 6:02:16 PM
1class Solution:
2    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
3        n=len(nums1)
4        d=defaultdict(list)
5        res=0
6        for i in range(n):
7            for j in range(n):
8                d[nums1[i]+nums2[j]].append((i,j))
9        for i in range(n):
10            for j in range(n):
11                req=0-(nums3[i]+nums4[j])
12                if req in d:
13                    res+=len(d[req])
14        return res
15                    