# Last updated: 6/13/2026, 1:30:28 PM
1class Solution:
2    def longestCycle(self, edges: List[int]) -> int:
3        v = set()  # Global memory: Have we ever fully processed this node?
4        longest = -1
5        
6        # We don't need a recursive dfs() function since there are no branching paths!
7        for i in range(len(edges)):
8            if i in v:
9                continue
10                
11            # Start a fresh stopwatch path for this specific walk
12            pathstck = {}
13            curr = i
14            steps = 0
15            
16            # March forward along the single directed path
17            while curr != -1:
18                # CASE 1: We hit a node in our CURRENT walk -> True Cycle!
19                if curr in pathstck:
20                    longest = max(longest, steps - pathstck[curr])
21                    break
22                    
23                # CASE 2: We hit a node from a PREVIOUS walk -> Dead end intersection
24                if curr in v:
25                    break
26                    
27                # Record the node's arrival time in our active path
28                pathstck[curr] = steps
29                
30                # Move to the next node
31                curr = edges[curr]
32                steps += 1
33                
34            # Once this path terminates or loops, mark all nodes seen in this walk 
35            # as permanently visited so we never waste time re-processing them.
36            for node in pathstck:
37                v.add(node)
38                
39        return longest