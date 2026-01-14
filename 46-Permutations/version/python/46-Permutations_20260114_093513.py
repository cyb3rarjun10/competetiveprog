# Last updated: 1/14/2026, 9:35:13 AM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        n = len(nums)
4        res = []
5
6        # queue holds (path, visited)
7        q = deque()
8        q.append(([], [False] * n))
9
10        while q:
11            path, visited = q.popleft()   # FIFO → BFS
12
13            if len(path) == n:
14                res.append(path)
15                continue
16
17            for i in range(n):
18                if not visited[i]:
19                    newpath = path + [nums[i]]
20                    newvisited = visited[:]
21                    newvisited[i] = True
22                    q.append((newpath, newvisited))
23
24        return res
25