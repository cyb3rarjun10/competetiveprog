# Last updated: 4/3/2026, 9:38:09 AM
1class Solution:
2    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
3        n = len(robots)
4        walls.sort() 
5        
6        roboda = []
7        for i in range(len(robots)):
8            roboda.append((robots[i], distance[i]))
9        roboda.sort(key=lambda x: x[0])
10        
11        # UPGRADED HELPER: Protected against overlapping edges
12        def count_new_walls(lb, rb, clearedupto):
13            if lb > rb: return 0
14            
15            # Find index of the first wall STRICTLY greater than what we've already cleared
16            cleared_idx = bisect.bisect_right(walls, clearedupto)
17            
18            # Find index of the first wall in our physical shooting range
19            lb_idx = bisect.bisect_left(walls, lb)
20            
21            # Our true starting point is whichever index is further to the right
22            start_idx = max(lb_idx, cleared_idx)
23            
24            # Find index strictly after our physical right bound
25            end_idx = bisect.bisect_right(walls, rb)
26            
27            return max(0, end_idx - start_idx)
28
29        @cache
30        def recurse(idx, clearedupto):
31            if idx == n:
32                return 0
33            
34            pos, dist = roboda[idx]
35            
36            # --- LEFT SHOOT ---
37            left_reach = pos - dist
38            if idx - 1 >= 0:
39                left_reach = max(roboda[idx-1][0], left_reach)
40
41            # We just pass our physical bounds and let the helper exclude the cleared stuff
42            leftwalls = count_new_walls(left_reach, pos, clearedupto)
43            
44            # We cleared everything up to 'pos'
45            leftscore = leftwalls + recurse(idx + 1, max(clearedupto, pos))
46            
47            # --- RIGHT SHOOT ---
48            right_reach = pos + dist
49            if idx + 1 < n:
50                right_reach = min(roboda[idx+1][0], right_reach)
51                
52            rightwalls = count_new_walls(pos, right_reach, clearedupto)
53            
54            # We cleared everything up to 'right_reach'
55            rightscore = rightwalls + recurse(idx + 1, max(right_reach, clearedupto))
56
57            return max(leftscore, rightscore)
58            
59        return recurse(0, float('-inf'))