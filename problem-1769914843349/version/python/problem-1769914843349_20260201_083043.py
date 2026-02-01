# Last updated: 2/1/2026, 8:30:43 AM
1class RideSharingSystem:
2
3    def __init__(self):
4        self.riders=deque()
5        self.drivers=deque()
6        self.activeriders=set()
7
8    def addRider(self, riderId: int) -> None:
9        self.riders.append(riderId)
10        self.activeriders.add(riderId)
11
12    def addDriver(self, driverId: int) -> None:
13        self.drivers.append(driverId)
14        
15    def matchDriverWithRider(self) -> List[int]:
16        while self.riders and self.riders[0] not in self.activeriders:
17            self.riders.popleft()
18        if not self.riders or not self.drivers:
19            return [-1,-1]
20        matched_driver=self.drivers.popleft()
21        matched_rider=self.riders.popleft()
22        self.activeriders.remove(matched_rider)
23        return [matched_driver,matched_rider]
24
25    def cancelRider(self, riderId: int) -> None:
26        if riderId in self.activeriders:
27            self.activeriders.remove(riderId)
28
29
30# Your RideSharingSystem object will be instantiated and called as such:
31# obj = RideSharingSystem()
32# obj.addRider(riderId)
33# obj.addDriver(driverId)
34# param_3 = obj.matchDriverWithRider()
35# obj.cancelRider(riderId)