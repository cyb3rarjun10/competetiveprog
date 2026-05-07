# Last updated: 5/7/2026, 6:35:56 PM
1class Solution:
2    def maxValue(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5        # [value, left, right]
6        stack = []
7
8        for i in range(n):
9            curr_val = nums[i]
10            curr_left = i
11            curr_right = i
12
13            while stack and stack[-1][0] > nums[i]:
14                top_val, top_left, top_right = stack.pop()
15                curr_val = max(curr_val, top_val)
16                curr_left = top_left
17
18            stack.append((curr_val, curr_left, curr_right))
19
20        for i in range(len(stack)):
21            for j in range(stack[i][1], stack[i][2] + 1):
22                ans[j] = stack[i][0]
23
24        return ans