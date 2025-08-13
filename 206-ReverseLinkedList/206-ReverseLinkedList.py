# Last updated: 8/12/2025, 9:16:27 PM
class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
