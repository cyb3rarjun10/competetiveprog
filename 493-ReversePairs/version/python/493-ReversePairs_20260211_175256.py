# Last updated: 2/11/2026, 5:52:56 PM
1class Solution:
2    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
3        people.sort(key=lambda p:(-p[0],p[1]))
4        res=[]
5        for p in people:
6            res.insert(p[1],p)
7        return res