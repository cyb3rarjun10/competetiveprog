# Last updated: 4/1/2026, 6:00:14 PM
1class Solution:
2    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
3        n = len(positions)
4        indices = list(range(n))
5        result = []
6        stack = deque()
7
8        # Sort indices based on their positions
9        indices.sort(key=lambda x: positions[x])
10
11        for current_index in indices:
12            # Add right-moving robots to the stack
13            if directions[current_index] == "R":
14                stack.append(current_index)
15            else:
16                while stack and healths[current_index] > 0:
17                    # Pop the top robot from the stack for collision check
18                    top_index = stack.pop()
19
20                    if healths[top_index] > healths[current_index]:
21                        # Top robot survives, current robot is destroyed
22                        healths[top_index] -= 1
23                        healths[current_index] = 0
24                        stack.append(top_index)
25                    elif healths[top_index] < healths[current_index]:
26                        # Current robot survives, top robot is destroyed
27                        healths[current_index] -= 1
28                        healths[top_index] = 0
29                    else:
30                        # Both robots are destroyed
31                        healths[current_index] = 0
32                        healths[top_index] = 0
33
34        # Collect surviving robots
35        for index in range(n):
36            if healths[index] > 0:
37                result.append(healths[index])
38
39        return result