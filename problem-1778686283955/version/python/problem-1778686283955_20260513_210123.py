# Last updated: 5/13/2026, 9:01:23 PM
1class Solution:
2    def minMoves(self, nums: List[int], limit: int) -> int:
3        n = len(nums)
4        sum_count = Counter()
5        min_arr = []
6        max_arr = []
7
8        for i in range(n // 2):
9            a = min(nums[i], nums[n - 1 - i])
10            b = max(nums[i], nums[n - 1 - i])
11
12            sum_count[a + b] += 1
13            min_arr.append(a)
14            max_arr.append(b)
15
16        min_arr.sort()
17        max_arr.sort()
18
19        min_ops = n
20
21        for c in range(2, 2 * limit + 1):
22            add_left = n // 2 - bisect_left(min_arr, c)
23            add_right = bisect_left(max_arr, c - limit)
24
25            current_ops = n // 2 + add_left + add_right - sum_count[c]
26            min_ops = min(min_ops, current_ops)
27
28        return min_ops