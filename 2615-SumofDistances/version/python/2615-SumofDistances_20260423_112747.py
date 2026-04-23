# Last updated: 4/23/2026, 11:27:47 AM
1class Solution:
2    def distance(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5
6        mp = defaultdict(list)
7
8        for i, v in enumerate(nums):
9            mp[v].append(i)
10
11        for pos in mp.values():
12            total = sum(pos)
13            left_sum = 0
14            m = len(pos)
15
16            for i in range(m):
17                right_sum = total - left_sum - pos[i]
18
19                left = pos[i] * i - left_sum
20                right = right_sum - pos[i] * (m - i - 1)
21
22                ans[pos[i]] = left + right
23
24                left_sum += pos[i]
25
26        return ans