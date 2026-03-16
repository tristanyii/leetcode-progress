# Last updated: 3/15/2026, 8:30:22 PM
1class Solution:
2    def hasCycle(self, head: Optional[ListNode]) -> bool:
3        slow = head
4        fast = head
5        
6        while fast and fast.next:
7            slow = slow.next
8            fast = fast.next.next
9            
10            if slow == fast:
11                return True
12        
13        return False