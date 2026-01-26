# Last updated: 1/26/2026, 9:25:35 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        queue=deque([])
4        res=[]
5        n=len(nums)
6        for i in range(n):
7            if queue and queue[0]<=i-k:
8                queue.popleft()
9            while queue and nums[queue[-1]]<=nums[i]:
10                queue.pop()
11            queue.append(i)
12            if i>=k-1:
13                res.append(nums[queue[0]])
14        return res
15        
16