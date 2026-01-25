# Last updated: 1/25/2026, 8:20:43 AM
1class Solution:
2    def rotateElements(self, nums: List[int], k: int) -> List[int]:
3        posielts=[i for i in nums if i>=0]
4        l=len(posielts)
5        if l>0:
6            k%=l
7        elts=posielts[k:]+posielts[:k]
8        idx=0
9        for i in range(len(nums)):
10            if nums[i]>=0:
11                nums[i]=elts[idx]
12                idx+=1
13        return nums