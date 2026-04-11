# Last updated: 4/11/2026, 8:45:13 PM
1class Solution:
2    def trafficSignal(self, timer: int) -> str:
3        if timer==0:
4            return "Green"
5        elif timer==30:
6            return "Orange"
7        elif timer>30 and timer<=90:
8            return "Red"
9        else:
10            return "Invalid"