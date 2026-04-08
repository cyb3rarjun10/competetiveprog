# Last updated: 4/8/2026, 11:03:36 PM
1class Solution:
2    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
3        for i in range(len(queries)):
4            query=queries[i]
5            l=query[0]
6            r=query[1]
7            k=query[2]
8            v=query[3]
9            idx=l
10            while idx<=r:
11                nums[idx]=(nums[idx]*v) % ((10**9) + 7)
12                idx+=k
13        res=0
14        for i in nums:
15            res^=i
16        return res
17            
18                