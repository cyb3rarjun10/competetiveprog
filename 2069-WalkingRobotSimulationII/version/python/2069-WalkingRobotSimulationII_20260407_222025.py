# Last updated: 4/7/2026, 10:20:25 PM
1class Robot:
2
3    def __init__(self, width: int, height: int):
4        self.x = 0
5        self.y = 0
6        self.w = width
7        self.h = height
8        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
9        self.perimeter = 2 * (width + height) - 4
10
11    def step(self, num: int) -> None:
12        if self.perimeter == 0:
13            return
14        
15        num %= self.perimeter
16        
17        # Special case: if num == 0, robot should face South at (0,0)
18        if num == 0:
19            if self.x == 0 and self.y == 0:
20                self.dir = 3
21            return
22
23        while num > 0:
24            if self.dir == 0:  # East
25                steps = min(num, self.w - 1 - self.x)
26                self.x += steps
27            elif self.dir == 1:  # North
28                steps = min(num, self.h - 1 - self.y)
29                self.y += steps
30            elif self.dir == 2:  # West
31                steps = min(num, self.x)
32                self.x -= steps
33            else:  # South
34                steps = min(num, self.y)
35                self.y -= steps
36
37            num -= steps
38
39            if num > 0:
40                self.dir = (self.dir + 1) % 4
41
42    def getPos(self):
43        return [self.x, self.y]
44
45    def getDir(self):
46        return ["East", "North", "West", "South"][self.dir]