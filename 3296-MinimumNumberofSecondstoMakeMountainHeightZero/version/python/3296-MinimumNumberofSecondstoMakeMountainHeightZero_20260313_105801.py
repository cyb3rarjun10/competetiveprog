# Last updated: 3/13/2026, 10:58:01 AM
1class Solution:
2    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
3        def possible(time):#(time alloted to each worked)
4            k=mountainHeight
5            for w in workerTimes:
6                val=(2*time)//w
7                n=math.isqrt(val)
8                if n*(n+1)>val:
9                    n-=1
10                k-=n
11                if k<=0:
12                    return True
13            return False
14
15
16        left=1
17        max_w=max(workerTimes)
18        right=max_w * mountainHeight * (mountainHeight + 1) // 2
19        while left<right:
20            mid=(left+right)//2
21            if possible(mid):
22                right=mid
23            else:
24                left=mid+1
25        return left
26