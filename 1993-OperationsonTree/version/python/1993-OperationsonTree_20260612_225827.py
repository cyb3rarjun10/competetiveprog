# Last updated: 6/12/2026, 10:58:27 PM
1class LockingTree:
2
3    def __init__(self, parent: List[int]):
4        self.parent=parent
5        self.locked=[None]*len(parent)
6        self.child={i:[] for i in range(len(parent))}
7
8        for i in range(len(parent)):
9            if parent[i]!=-1:
10                self.child[parent[i]].append(i)
11
12
13    def lock(self, num: int, user: int) -> bool:
14        if self.locked[num]:
15            return False
16        self.locked[num]=user
17        return True
18
19    def unlock(self, num: int, user: int) -> bool:
20        if not self.locked[num]:
21            return False
22        elif self.locked[num]==user:
23            self.locked[num]=None
24            return True
25        else:
26            return False
27        
28
29    def upgrade(self, num: int, user: int) -> bool:
30
31        #check ancestors 
32        i=num
33        while i!=-1:
34            if self.locked[i]:
35                return False
36            i=self.parent[i]
37        
38        #check descendants and unlock
39        #count->(count of locked descendants)
40
41        count=0
42        q=deque([num])
43        while q:
44            x=q.popleft()
45            if self.locked[x]:
46                self.locked[x]=None
47                count+=1
48            q.extend(self.child[x])
49        if count == 0:
50            return False
51
52        self.locked[num] = user
53        return True
54
55
56
57# Your LockingTree object will be instantiated and called as such:
58# obj = LockingTree(parent)
59# param_1 = obj.lock(num,user)
60# param_2 = obj.unlock(num,user)
61# param_3 = obj.upgrade(num,user)