# Last updated: 5/11/2026, 5:27:57 PM
1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        res=[]
4        for i in nums:
5            x=str(i)
6            for k in x:
7                res.append(int(k))
8        return res