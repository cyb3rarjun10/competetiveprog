# Last updated: 4/5/2026, 8:16:45 AM
1class Solution:
2    def mirrorFrequency(self, s: str) -> int:
3        chmap={'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v','f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q','k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l','p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g','u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b','z': 'a'}
4        digmap = {i: 9 - i for i in range(10)}
5        v=set()
6        d=defaultdict(int)
7        for i in s:
8            d[i]+=1
9        res=0
10        for ch in s:
11            if ch in v:
12                continue
13            if ch.isdigit():
14                cf=d[ch]
15                mf=d[str(digmap[int(ch)])]
16                v.add(str(digmap[int(ch)]))
17            else:
18                cf=d[ch]
19                mf=d[chmap[ch]]
20                v.add(chmap[ch])
21            v.add(ch)
22            res+=abs(cf-mf)
23        return res
24            
25            
26            
27