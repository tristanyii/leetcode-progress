# Last updated: 10/6/2025, 6:03:44 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False

        prev = head
        penis = head.next


        while penis and penis.next != None: 
            if penis == prev:
                return True
            prev = prev.next
            penis = penis.next.next
        return False
            
                

        
        