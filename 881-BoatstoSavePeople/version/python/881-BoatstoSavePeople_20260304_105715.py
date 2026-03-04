# Last updated: 3/4/2026, 10:57:15 AM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        n=len(people)
5        r=n-1
6        l=0
7        boats=0
8        while r>=l:
9            if people[r]+people[l]<=limit:
10                r-=1
11                l+=1
12            else:
13                r-=1
14            boats+=1
15        return boats
16
17