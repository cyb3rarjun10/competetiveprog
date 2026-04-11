# Last updated: 4/11/2026, 8:46:55 PM
1class Solution:
2    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
3        s=""
4        for num in nums:
5            s+=str(num)
6        res=0
7        k=str(digit)
8        for i in s:
9            if i==k:
10                res+=1
11        return res
12                