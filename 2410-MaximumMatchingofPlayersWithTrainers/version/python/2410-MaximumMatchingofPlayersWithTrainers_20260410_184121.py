# Last updated: 4/10/2026, 6:41:21 PM
1class Solution:
2    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
3        players.sort()
4        trainers.sort()
5        n=len(players)
6        m=len(trainers)
7        pi=0
8        ti=0
9        res=0
10        while pi<n and ti<m:
11            while ti<m and trainers[ti]<players[pi]:
12                ti+=1
13            if ti<m:
14                pi+=1
15                ti+=1
16                res+=1
17        return res
18            