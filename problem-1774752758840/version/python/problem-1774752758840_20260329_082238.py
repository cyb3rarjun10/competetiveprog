# Last updated: 3/29/2026, 8:22:38 AM
1class EventManager:
2
3    def __init__(self, events: list[list[int]]):
4        self.events=events
5        self.heap=[]
6        self.d={}
7        for ev,pr in self.events:
8            self.d[ev]=pr
9            heapq.heappush(self.heap,(-pr,ev))
10
11    def updatePriority(self, eventId: int, newPriority: int) -> None:
12        self.d[eventId]=newPriority
13        heapq.heappush(self.heap,(-newPriority,eventId))
14        
15    def pollHighest(self) -> int:
16        while self.heap:
17            negpr,id=heapq.heappop(self.heap)
18            if id in self.d and self.d[id]==-negpr:
19                del self.d[id]
20                return id
21        return -1
22
23
24# Your EventManager object will be instantiated and called as such:
25# obj = EventManager(events)
26# obj.updatePriority(eventId,newPriority)
27# param_2 = obj.pollHighest()
28