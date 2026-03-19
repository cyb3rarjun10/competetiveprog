# Last updated: 3/19/2026, 5:18:01 PM
1class Solution:
2    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
3        diff=[0]*(n+1)
4        for l,r,seats in bookings:
5            diff[l-1]+=seats
6            diff[r]-=seats
7        curr=0
8        res=[]
9        for i in diff:
10            curr+=i
11            res.append(curr)
12        return res[:n]
13