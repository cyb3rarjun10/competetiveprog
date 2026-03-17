# Last updated: 3/17/2026, 6:58:40 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        maxArea = 0
5        n = len(heights)
6
7        for i in range(n + 1):
8            h = 0 if i == n else heights[i]
9            while stack and h < heights[stack[-1]]:
10                height = heights[stack.pop()]
11                width = i if not stack else i - stack[-1] - 1
12                maxArea = max(maxArea, height * width)
13            stack.append(i)
14
15        return maxArea