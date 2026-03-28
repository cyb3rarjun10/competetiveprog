# Last updated: 3/28/2026, 8:03:30 PM
1class Solution:
2    def minAbsoluteDifference(self, nums: list[int]) -> int:
3        one=[]
4        two=[]
5        for i in range(len(nums)):
6            if nums[i]==1:
7                one.append(i)
8            elif nums[i]==2:
9                two.append(i)
10        if len(one)==0 or len(two)==0:
11            return -1
12        minlen=float('inf')
13        for i in one:
14            for j in two:
15                minlen=min(minlen,abs(i-j))
16        return minlen
17        