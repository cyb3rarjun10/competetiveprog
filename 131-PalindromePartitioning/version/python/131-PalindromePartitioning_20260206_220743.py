# Last updated: 2/6/2026, 10:07:43 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        n=len(nums)
5        def backtrack(i,curr):
6            if i==n:
7                res.append(curr[:])
8                return
9            #exclude
10            backtrack(i+1,curr)
11
12            #include
13            curr.append(nums[i])
14            backtrack(i+1,curr)
15            curr.pop()
16        backtrack(0,[])
17        return res
18
19        
20
21
22
23            