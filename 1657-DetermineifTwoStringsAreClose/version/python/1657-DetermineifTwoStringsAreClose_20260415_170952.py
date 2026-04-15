# Last updated: 4/15/2026, 5:09:52 PM
1class Solution:
2    def closeStrings(self, word1: str, word2: str) -> bool:
3
4        d=Counter(word1)
5        e=Counter(word2)
6        a=set(word1)
7        b=set(word2)
8        at=0
9        bt=0
10        for i in a:
11            at+=ord(i)
12        for i in b:
13            bt+=ord(i)
14        if at!=bt:
15            return False
16        l1=list(d.values())
17        l2=list(e.values())
18
19        l1.sort()
20        l2.sort()
21
22        return l1==l2