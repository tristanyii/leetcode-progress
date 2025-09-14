# Last updated: 9/13/2025, 10:00:06 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode(None)
        curr = head
        
        while list1 or list2:
            if list1 is None:
                curr.next = list2
                return head.next
            if list2 is None:
                curr.next = list1
                return head.next
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return head.next


        
        