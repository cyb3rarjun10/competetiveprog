# Last updated: 4/23/2026, 11:26:02 AM
1class TrieNode:
2    def __init__(self):
3        self.child = [None] * 26
4        self.isEnd = False
5
6
7class Solution:
8    def __init__(self):
9        self.root = TrieNode()
10
11    def insert(self, word):
12        node = self.root
13        for c in word:
14            idx = ord(c) - ord("a")
15            if not node.child[idx]:
16                node.child[idx] = TrieNode()
17            node = node.child[idx]
18        node.isEnd = True
19
20    def dfs(self, word, i, node, cnt):
21        if cnt > 2 or not node:
22            return False
23
24        if i == len(word):
25            return node.isEnd
26
27        idx = ord(word[i]) - ord("a")
28
29        # no changes made
30        if node.child[idx] and self.dfs(word, i + 1, node.child[idx], cnt):
31            return True
32
33        # made changes
34        if cnt < 2:
35            for c in range(26):
36                if c == idx:
37                    continue
38                if node.child[c] and self.dfs(
39                    word, i + 1, node.child[c], cnt + 1
40                ):
41                    return True
42
43        return False
44
45    def twoEditWords(self, queries, dictionary):
46        for w in dictionary:
47            self.insert(w)
48
49        res = []
50        for q in queries:
51            if self.dfs(q, 0, self.root, 0):
52                res.append(q)
53        return res