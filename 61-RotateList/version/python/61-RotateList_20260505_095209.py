# Last updated: 5/5/2026, 9:52:09 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head:
9            return None
10        curr=head
11        n=1
12        while curr.next!=None:
13            curr=curr.next
14            n+=1
15        curr.next=head
16        newtail=head
17        k=k%n
18        for i in range(n-k-1):
19            newtail=newtail.next
20        newhead=newtail.next
21        newtail.next=None
22        return newhead