# Last updated: 4/13/2026, 9:53:38 PM
1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        n=len(nums)
4        left=0
5        c=0
6        maxlen=float('-inf')
7        for right in range(n):
8            if nums[right]==0:
9                c+=1
10            while c>1:
11                if nums[left]==0:
12                    c-=1
13                left+=1
14            maxlen=max(maxlen,right-left)
15        return maxlen