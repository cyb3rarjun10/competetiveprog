# Last updated: 3/11/2026, 10:03:55 AM
1class Solution:
2    def snakesAndLadders(self, board: List[List[int]]) -> int:
3        n=len(board)
4        k=n*n
5        def ladder_to_rc(num, n):
6            num -= 1                     # convert to 0-index
7
8            row = n - 1 - (num // n)     # find row
9            col = num % n                # base column
10
11            # reverse column if row direction is right->left
12            if (n - 1 - row) % 2 == 1:
13                col = n - 1 - col
14
15            return row, col
16        queue=deque([(1,0)])#(curr,dicerolled)
17        v=set([1])
18        while queue:
19            l=len(queue)
20            for _ in range(l):
21                curr,currsteps=queue.popleft()
22                if curr==k:
23                    return currsteps
24                for i in range(1,6+1):
25                    if curr+i>k:
26                        break
27                    if curr+i in v:
28                        continue
29                    r,c=ladder_to_rc(curr+i,n)
30                    if board[r][c]==-1:
31                        queue.append((curr+i,currsteps+1))
32                    else:
33                        queue.append((board[r][c],currsteps+1))
34                    v.add(curr+i)
35        return -1
36        
37                
38                
39            