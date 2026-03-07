# Last updated: 3/7/2026, 5:15:20 PM
1class Solution:
2    def minFlips(self, s: str) -> int:
3        n = len(s)
4        s = s + s
5        
6        # 1. Pre-build the two valid targets for the extended string length
7        alt1, alt2 = "", ""
8        for i in range(len(s)):
9            alt1 += "1" if i % 2 == 0 else "0"
10            alt2 += "0" if i % 2 == 0 else "1"
11            
12        res = float('inf')
13        diff1, diff2 = 0, 0
14        l = 0 # Left pointer for our window
15        
16        # 2. Slide the right pointer across the extended string
17        for r in range(len(s)):
18            # Add to our mismatch tally if the new character doesn't match
19            if s[r] != alt1[r]: diff1 += 1
20            if s[r] != alt2[r]: diff2 += 1
21            
22            # 3. If our window gets bigger than the original string length 'n', shrink it
23            if (r - l + 1) > n:
24                # Remove the left character from our tally if it was a mismatch
25                if s[l] != alt1[l]: diff1 -= 1
26                if s[l] != alt2[l]: diff2 -= 1
27                l += 1 # Slide left pointer forward
28                
29            # 4. If our window is exactly size 'n', record the minimum flips!
30            if (r - l + 1) == n:
31                res = min(res, diff1, diff2)
32                
33        return res
34