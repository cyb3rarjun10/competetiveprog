# Last updated: 1/11/2026, 8:51:46 AM
1class Solution:
2    def countPairs(self, words: List[str]) -> int:
3        count=0
4        n=len(words)
5        d=defaultdict(int)
6        for w in words:
7            ase=ord(w[0])-ord('a')
8            k=[]
9            for i in w:
10                x=ord(i)-ord('a')
11                k.append((x-ase)%26)
12            k=tuple(k)
13            count+=d[k]
14            d[k]+=1
15        return count
16                
17                