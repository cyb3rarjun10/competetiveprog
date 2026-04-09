# Last updated: 4/9/2026, 5:17:50 PM
1class Solution:
2    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
3        n = len(nums)
4        MOD = 10**9 + 7
5        limit = math.isqrt(n)
6        
7        # Group queries with small k for later processing
8        lightK = defaultdict(list)
9        
10        for q in queries:
11            l, r, k, v = q
12            
13            if k >= limit:
14                # Large k: apply brute force
15                for i in range(l, r + 1, k):
16                    nums[i] = (nums[i] * v) % MOD
17            else:
18                # Small k: process later
19                lightK[k].append(q)
20                
21        for k, query_list in lightK.items():
22            # Process small queries grouped by step size k
23            diff = [1] * n
24            
25            for q in query_list:
26                l, r, _, v = q
27                
28                # Multiply starting position
29                diff[l] = (diff[l] * v) % MOD
30                
31                # Cancel the multiplication using modular inverse
32                steps = (r - l) // k
33                nxt = l + (steps + 1) * k
34                if nxt < n:
35                    # pow(v, -1, MOD) computes the modular inverse natively
36                    diff[nxt] = (diff[nxt] * pow(v, -1, MOD)) % MOD
37                    
38            # Propagate the multipliers with a step size of k
39            for i in range(n):
40                if i >= k:
41                    diff[i] = (diff[i] * diff[i - k]) % MOD
42                nums[i] = (nums[i] * diff[i]) % MOD
43                
44        ans = 0
45        for num in nums:
46            ans ^= num
47            
48        return ans
49        