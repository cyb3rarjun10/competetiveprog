# Last updated: 3/9/2026, 11:31:20 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        n=len(s)
4        d=defaultdict(list)
5        for i in range(len(wordDict)):
6            d[wordDict[i][0]].append(i)
7        @cache
8        def recurse(idx):
9            if idx==n:
10                return True
11            char=s[idx]
12            if char not in d:
13                return False
14            indices=d[char]
15            for i in indices:
16                l=len(wordDict[i])
17                if s[idx:idx+l]==wordDict[i]:
18                    if recurse(idx+l):
19                        return True
20            return False
21        return recurse(0)
22