# Last updated: 4/12/2026, 8:29:08 AM
1class Solution:
2    def internalAngles(self, sides: list[int]) -> list[float]:
3        a=sides[0]
4        b=sides[1]
5        c=sides[2]
6        if a+b<=c or b+c<=a or a+c<=b:
7            return []
8        arad=acos((b**2+c**2 - a**2)/(2*b*c))
9        brad=acos((a**2+c**2 - b**2)/(2*a*c))
10        crad=acos((a**2+b**2 - c**2)/(2*a*b))
11
12        return sorted([math.degrees(arad),math.degrees(brad),math.degrees(crad)])
13        
14        