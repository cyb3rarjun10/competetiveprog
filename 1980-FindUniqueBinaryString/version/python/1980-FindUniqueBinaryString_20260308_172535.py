# Last updated: 3/8/2026, 5:25:35 PM
1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        s=set(nums)
4        n=len(nums[0])
5        stck=[(0,"")]
6        while stck:
7            idx,curr=stck.pop()
8            if idx==n:
9                if curr not in s:
10                    return curr
11                continue
12            stck.append((idx+1,curr+"1"))
13            stck.append((idx+1,curr+"0"))
14        return -1